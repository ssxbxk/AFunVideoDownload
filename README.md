AFun 视频下载工具

根据配置的AFun地址, 获取整个视频集列表, 按照列表上视频的顺序, 依次下载.

用法以及问题
1. 在main.py中添加要下载到本地的文件夹地址(path), 以及AFun站点的视频地址(url):
    hrefs = [
    #{"path":"XXX", "url":"https://www.acfun.cn/v/XXX"},
    #{"path":"XXXXX", "url":"https://www.acfun.cn/v/XXXXX"},
    ]
	
2. 执行run.bat

3. 已知的问题:
a. 未知原因, 某些视频, 获取不到m3u8文件地址;
b. 未知原因, 某些视频, 获取到m3u8内容后, 访问.ts地址时, 出现验证失败的情况;
c. 单线程运行, 下载比较慢, 只能起到减轻手工操作的作用.