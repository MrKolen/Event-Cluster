# -*- coding:utf8 -*-

import pandas as pd
import jieba
import collections


# 获取数据
def get_data():
    df = pd.read_table('../data/allSourceTextresult.txt', names=['Order', 'Time', 'Content'], encoding='UTF-8')
    content = df.Content.values.tolist()
    return content


# 分词
def segment_content():
    content_raw = get_data()
    content_sentence = []
    for line in content_raw:
        current_segment = jieba.lcut(line)
        if len(current_segment) > 1 and current_segment != '\r\n':
            content_sentence.append(current_segment)
    return content_sentence


# 分词后的句子
contents = pd.DataFrame({'content_sentence': segment_content()})

# 导入停用词
stopwords = pd.read_csv('stopwords.txt', sep='\t', index_col=False, quoting=3, names=['stopwords'], encoding='UTF-8')

contents = contents.content_sentence.values.tolist()
stopwords = stopwords.stopwords.values.tolist()


# 去停用词
def drop_stopwords(contents, stopwords):
    contents_cleaned = []
    all_words = []
    for line in contents:
        line_cleaned = []
        for word in line:
            if word in stopwords:
                continue
            line_cleaned.append(word)
            all_words.append(str(word))
        contents_cleaned.append(line_cleaned)
    return contents_cleaned, all_words


contents_clean, all_words = drop_stopwords(contents, stopwords)
contents_clean = pd.DataFrame({'contents_clean': contents_clean})

# # 统计词频，优化停用词
# counter = collections.Counter([tk for st in contents_clean.contents_clean for tk in st])
# counter = dict(filter(lambda x: x[1] >= 5, counter.items()))
# print(sorted(counter.items(), key=lambda item: item[1], reverse=True))

df_train = contents_clean['contents_clean'].values
words = []
for line_index in range(len(df_train)):
    try:
        words.append(' '.join(df_train[line_index]))
    except:
        print(line_index)
