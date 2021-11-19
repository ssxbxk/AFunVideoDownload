import re
from tqdm import tqdm
import os
from bs4 import BeautifulSoup
from utils import get_page_resp

def change_title(title):
    pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
    new_title = re.sub(pattern, "_", title)  # 替换为下划线
    return new_title


def save(name, video, title):
    path = f'{name}\\'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + title + '.ts', mode='wb') as f:
        f.write(video)


def get_m3u8_url(html_url, title):
    new_title = change_title(title) + '.mp4'
    if os.path.exists(new_title):
        print('文件已经存在: ' + new_title)
        return True

    print(f'开始下载 {title}')
    f = open(new_title, 'wb')
    url = 'https://www.acfun.cn' + html_url
    html_data = get_page_resp(url).text
    m3u8_url = ""
    try:
        m3u8_url = re.findall('backupUrl(.*?)\"]', html_data)[0].replace('"', '').split('\\')[-2]
    except:
        f.close()
        print('url地址不对!')
        print(re.findall('backupUrl(.*?)\"]', html_data))
        print('-------!')
        return False
    #tmp = re.findall('representation(.*?)\"]', html_data)[0]
    #m3u8_url = tmp.replace('"', '').split('\\')[-2]
    
    m3u8_data = get_page_resp(m3u8_url).text
    m3u8_data = re.sub('#EXTM3U', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-VERSION:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-TARGETDURATION:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-MEDIA-SEQUENCE:\d', "", m3u8_data)
    m3u8_data = re.sub(r'#EXT-X-ENDLIST', "", m3u8_data)
    m3u8_data = re.sub(r'#EXTINF:\d\.\d+?,', "", m3u8_data)
    m3u8 = m3u8_data.split()

    
    for link in tqdm(m3u8):
        ts_url = 'https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/hls/' + link
        video = get_page_resp(ts_url).content
        if len(video) == 0:
            print('无法获取到内容!' + ts_url)
            f.close()
            return False
        #ts_title = link.split('?')[0].split('.')[1]
        #save(new_title, video, ts_title)
        f.write(video)
    print(f'{title}已经下载完成')
    f.close()
    return True


def get_id_list(resp):
    soup = BeautifulSoup(resp, 'lxml')
    li = soup.find_all('li', class_='single-p')
    ret = []
    for i in range(0, len(li)):
        retObj = {"title":li[i].attrs["title"],"href":li[i].attrs["data-href"]}
        ret.append(retObj)
    return ret


def get_all_video(url, one_title, root_path):
    resp = get_page_resp(url).text
    video_list = get_id_list(resp)
    if len(video_list) > 0:
        for i in video_list:
            os.chdir(root_path)
            get_m3u8_url(i["href"], i["title"])
            #get_and_convert(os.getcwd() + "/" + i["title"], i["title"] + '.mp4', False)
    else:
        os.chdir(root_path)
        get_m3u8_url(url, one_title)
        #get_and_convert(os.getcwd() + "/" + one_title, one_title + '.mp4', False)

if __name__ == '__main__':
    pass