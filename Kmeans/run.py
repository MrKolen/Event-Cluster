# -*- coding:utf8 -*-
import os
import sys
import time
from Kmeans.cluster import k_means_model
from Kmeans.merge_files import merge_txt

if __name__ == '__main__':
    START_TIME = time.time()

    # 合并数据文件, 获得文档索引列表
    FILEPATH = "../data/allSourceText"
    OUTFILE = "result.txt"
    idx_to_doc = merge_txt(FILEPATH, OUTFILE)

    # 事件文档聚类
    labels = k_means_model()
    for file_idx in range(len(labels)):
        file_path = '../ClusterResult/' + str(labels[file_idx])
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(file_path + '/' + idx_to_doc[file_idx], 'a+', encoding='UTF-8') as k:
            txt_path = FILEPATH + '/' + idx_to_doc[file_idx]
            with open(txt_path, encoding='UTF-8') as f:
                k.write("[label: " + str(labels[file_idx]) + ']\n')
                for line in f.readlines():
                    if line == '\n':
                        continue
                    k.writelines(line)

    END_TIME = time.time()
    print('总共耗时：%.9fs' % (END_TIME - START_TIME))
