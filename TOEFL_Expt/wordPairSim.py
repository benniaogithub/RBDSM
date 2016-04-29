#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: wordPairSim.py
@time: 2016/4/28 4:14
"""

import numpy as np
from scipy import stats
import scipy.io as sio

def vecSim(x, y):
    # result1 = x.T.dot(y)
    # result1 =  result1.tolist()[0][0]           #svd 之前的稀疏原始矩阵用这个

    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):
        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim

def wordlantCosSim(w1,w2):
     # root=u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_300_TFIDF/rel_svd/file_word_lus/word_matus_latent_300/"

     root = u"I:/数据/word11247relation30/rel_30_ref_5000/rel_svd_TFIDF/file_word_lus/word_matus_latent_350/"
     #
     # w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     # w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     sim = 0.0

     for i in range(0,np.shape(w1Mat)[1]):         #单词按参考词的条件概率   一列一列算相似度
        sim = vecSim(w1Mat[:,i],w2Mat[:,i])+sim
        # print sim/np.shape(w1Mat)[1]
     return sim/np.shape(w1Mat)[1]
