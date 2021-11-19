# -*- coding:utf-8 -*- 
import sys 
import os 
from glob import glob 

#获取需要转换的路径 
def get_user_path(argv_dir): 
    if os.path.isdir(argv_dir): 
        return argv_dir 
    elif os.path.isabs(argv_dir): 
        return argv_dir 
    else: 
        return False

#对转换的TS文件进行排序         
def get_sorted_ts(user_path): 
    ts_list = glob(os.path.join(user_path,'*.ts')) 
    #print(ts_list) 
    boxer = [] 
    for ts in ts_list: 
        if os.path.exists(ts): 
            #print(os.path.splitext(os.path.basename(ts))) 
            file, _ = os.path.splitext(os.path.basename(ts))
            try:
                iFn = int(file)
                boxer.append(file)
            except:
                print('invalid file %s' % file)
    boxer.sort() 
    #print(boxer) 
    return boxer 

#文件合并     
def convert_m3u8(boxer, o_file_name, delete_file): 
    tmp = []
    idx = 0
    for ts in boxer:
        idx += 1
        tmp.append(str(ts)+'.ts')
        if idx >= 50:
            cmd_str = ' + '.join(tmp) 
            exec_str = "copy /b " + cmd_str + ' ' + o_file_name 
            os.system(exec_str)
            idx = 0
            tmp = [o_file_name]

    if idx > 0:
        cmd_str = ' + '.join(tmp) 
        exec_str = "copy /b " + cmd_str + ' ' + o_file_name 
        os.system(exec_str)

    if delete_file:
        for i in tmp:
            os.remove(i)

def get_and_convert(user_path, filename, delete_file=False):
    os.chdir(user_path) 
    boxer = get_sorted_ts(user_path) 
    convert_m3u8(boxer, filename, delete_file) 

if __name__=='__main__': 
    get_and_convert("D:/Study/Python/m3u8/1/", "1.mp4", True)