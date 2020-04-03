# -*- coding:utf-8*-

import os


# 合并同一个文件夹下多个txt
def merge_txt(file_path, out_file):
    # 建立文档索引
    idx_to_doc = []

    result_file_path = file_path + out_file
    # 文件存在则删除
    if os.path.exists(result_file_path):
        os.remove(result_file_path)
    with open(result_file_path, 'a+', encoding='UTF-8') as k:
        file_num = 0
        for parent, _, filenames in os.walk(file_path):
            for file_path in filenames:
                idx_to_doc.append(file_path)
                txt_path = os.path.join(parent, file_path)  # txt_path就是所有文件夹的路径
                with open(txt_path, encoding='UTF-8') as f:
                    # 给文件编号
                    file_num += 1
                    k.write(str(file_num) + '\t' + f.readline().strip() + '\t')
                    # 按行读取
                    for line in f.readlines():
                        if line == '\n':  # 去除文件中的空行
                            continue
                        k.writelines(line.strip() + " ")  # 把末尾的'\n'删掉, 并用空格分隔原文每行
                    k.write('\n')
    print("File Merging Complete")
    return idx_to_doc

