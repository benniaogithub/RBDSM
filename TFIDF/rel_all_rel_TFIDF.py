#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: rel_30_ref_TFIDF.py
@time: 2016/4/26 22:59
"""
import scipy.io as sio
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist

def rel_30_ref_TFIDF():                      #每个relation-ref 表做一次tfidf
    relpath = u"I:/数据/word11247relation30/rel_30_ref_all_mat/rel_30_ref_all_mat/result.mat"
    dest = u"I:/数据/word11247relation30/rel_30_ref_all_mat/rel_30_ref_all_mat/"
    if not os.path.exists(dest):
                os.makedirs(dest)
    rellist = getRelList()
    transformer = TfidfTransformer()
    relmat = sio.loadmat(relpath)["result"]
    tfidf = transformer.fit_transform(relmat)
    relTFIDF = tfidf.toarray()
    print relTFIDF.shape
    sio.savemat(dest+"TFIDF_result.mat",{"result":relTFIDF},oned_as='column')

rel_30_ref_TFIDF()