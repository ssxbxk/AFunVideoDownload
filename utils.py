import requests
from fake_useragent import UserAgent

page_headers={"Referer": "https://www.acfun.cn/"}

def get_page_resp(url):
    page_headers["User-Agent"] = UserAgent(use_cache_server=False).random
    resp = requests.get(url, headers=page_headers)
    return resp


if __name__ == "__main__":
    resp = get_page_resp('https://www.acfun.cn/v/ac27343761_1')