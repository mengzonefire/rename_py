# -*- coding: UTF-8 -*-
import traceback
import locale
import os
path = os.getcwd()
Action_Get_List = False
Action_Rename_File = True
file_list = []
rename_list = []
exe_path, exe_name = os.path.split(__file__)


def get_file_list():
    global file_list
    file_list = os.listdir(path)
    file_list.remove(exe_name)
    file_list = sorted(file_list, key=locale.strxfrm)
    if "list.txt" in file_list:
        file_list.remove('list.txt')
        return Action_Rename_File
    else:
        return Action_Get_List


def write_list_file(m_list):
    with open('list.txt', 'w', encoding='utf-8') as f:
        for file in m_list:
            f.write(file + '\n')


def read_list_file():
    global rename_list
    with open('list.txt', 'r', encoding='utf-8') as f:
        rename_list = f.read()
        rename_list = rename_list.split('\n')
        rename_list.remove('')


def write_error_file(error_log):
    with open('error_log.txt', 'w', encoding='utf-8') as f:
        f.write(error_log)


def main():
    global file_list, rename_list
    locale.setlocale(locale.LC_ALL, locale='zh-CN')
    if Action_Rename_File == get_file_list():
        read_list_file()
        if len(rename_list) == len(file_list):
            for i in range(0, len(rename_list)):
                os.rename(file_list[i], rename_list[i])
            write_list_file(sorted(rename_list, key=locale.strxfrm))
        else:
            write_error_file("文件数量与目录不匹配，请删除list.txt再重新运行程序")
    elif Action_Get_List == get_file_list():
        write_list_file(file_list)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        write_error_file(e)
