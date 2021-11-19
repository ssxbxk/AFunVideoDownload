from AfunGet import get_all_video
import os

if __name__ == "__main__":
    hrefs = [
    #{"path":"2021昭昭病史采集", "url":"https://www.acfun.cn/v/ac27343761_1"},
    #{"path":"2021昭昭考前串讲", "url":"https://www.acfun.cn/v/ac30985131"},
    #{"path":"2021昭昭早读课", "url":"https://www.acfun.cn/v/ac30984820"},
    #{"path":"2021昭昭真题解析", "url":"https://www.acfun.cn/v/ac30143658"},
    #{"path":"2021技能直播课", "url":"https://www.acfun.cn/v/ac28876912"},
    #{"path":"2021技能基本操作", "url":"https://www.acfun.cn/v/ac28537128"},
    #{"path":"2021技能上机考试部分", "url":"https://www.acfun.cn/v/ac28537070"},
    #{"path":"2021昭昭技能体格检查", "url":"https://www.acfun.cn/v/ac27686541"},
    #{"path":"2021昭昭技能病例分析", "url":"https://www.acfun.cn/v/ac27588822"},
    #{"path":"2021导学课", "url":"https://www.acfun.cn/v/ac20759934"}
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