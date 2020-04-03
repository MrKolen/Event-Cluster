# -*- coding:utf8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from Kmeans.data_processing import words


# 转化为TF-IDF向量
def tf_idf_vector():
    vectorizer = TfidfVectorizer(max_features=4000, lowercase=False)
    vectorizer.fit(words)
    return vectorizer.transform(words)


# K-Means聚类模型
def k_means_model():
    vector = tf_idf_vector()
    km_model = KMeans(n_clusters=5)  # 实例化聚类器
    km_model.fit(vector)  # 传入特征数据
    label_pred = km_model.labels_  # 获取聚类标签
    return label_pred

