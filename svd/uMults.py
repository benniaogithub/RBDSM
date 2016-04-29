#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: uMults.py
@time: 2016/4/26 18:55
"""
import scipy.io as sio
import os
import numpy as np

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    # arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist
def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)

    return  wordList

def us(dim):                        #svd 后的 u 矩阵和s 矩阵相乘
    relpath = u"I:/数据/word11247relation30/rel_matrix_ls/rel_mat_latent_"
    relpath = relpath+str(dim)+u"/"
    relspath = u"I:/数据/word11247relation30/rel_matrix_s/rel_mat_latent_"
    relspath = relspath+str(dim)+u"/"
    dest = u"I:/数据/word11247relation30/rel_matrix_lus/rel_mat_latent_"
    dest = dest+str(dim)+u"/"
    rellist = getRelList()
    if not os.path.exists(dest):
                os.makedirs(dest)
    for i in range(0,len(rellist)):
            rel = rellist[i]
            print rel
            relmat = sio.loadmat(relpath+"r_"+rel+".mat")[rel]
            relsmat = sio.loadmat(relspath+"r_"+rel+".mat")[rel].T
            relusmat = relmat*relsmat
            # print relsmat
            # print relsmat.shape
            # relusmat = relmat.dot(relsmat)
            sio.savemat(dest+"r_"+rel+".mat",{rel:relusmat},oned_as='column')

us(100)