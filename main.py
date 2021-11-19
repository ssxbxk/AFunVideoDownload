from AfunGet import get_all_video
import os

if __name__ == "__main__":
    hrefs = [
    #{"path":"XXX", "url":"https://www.acfun.cn/v/XXX"},
    #{"path":"XXXXX", "url":"https://www.acfun.cn/v/XXXXX"},
    ]

    url_root = os.getcwd() + '\\download'
    if not os.path.exists(url_root):
        os.makedirs(url_root)

    for href in hrefs:
        sub_path = url_root + "\\" + href["path"]
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)
        
        os.chdir(sub_path)
        get_all_video(href["url"], href["path"], sub_path)