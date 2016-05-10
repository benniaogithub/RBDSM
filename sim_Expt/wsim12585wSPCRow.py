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
np.set_printoptions(threshold='nan')

def getWTFIDF():
    wArr = sio.loadmat(u"I:/数据/word12585relation30/weight/wTFIDF2.mat")["wTFIDF"][0]
    # print(wArr)
    # arr = np.array(wordList)
    return  wArr

wArr = getWTFIDF()
def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def vecSimRow(x, y):
    # result1 = x.T.dot(y)
    # result1 =  result1.tolist()[0][0]           #svd 之前的稀疏原始矩阵用这个

    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):
        # print "fdddd"
        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim

def wordlantCosSimRow(w1,w2):
     root = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"

     # root = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"
     # root = u"I:/数据/word12585relation30/rel_30_ref_5000/rel_svd/file_word_lus/word_mat_latent_350/"
     #
     # w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     # w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     # print(w1Mat)
     w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     sim = 0.0
     print np.shape(w1Mat)[0]
     for i in range(0,np.shape(w1Mat)[0]):         #单词按参考词的条件概率   一列一列算相似度
        sim = vecSimRow(w1Mat[i,:],w2Mat[i,:])*wArr[i]+sim
        # print sim/np.shape(w1Mat)[1]
     return sim

     # for i in range(0,np.shape(w1Mat)[1]):         #单词按参考词的条件概率   一列一列算相似度
     #    sim = vecSim(w1Mat[:,i],w2Mat[:,i])+sim
     #    # print sim/np.shape(w1Mat)[1]
     # return sim/np.shape(w1Mat)[1]
def SCTRow():

    wslist = []
    sdsmlist = []
    count = 1
    wordList = getWordList()
    for line in open("../res/WS-353.txt"):
        w1 = line.split("\t")[0]
        w2 = line.split("\t")[1]
        if w1 in wordList and w2 in wordList:
            sim1 = wordlantCosSimRow(w1,w2)
            # print(sim1)
            sim2 = line.strip("\n").split("\t")[-1]
            # print sim2
            wslist.append(sim1)
            sdsmlist.append(sim2)
            print count
            count += 1
    rho, pval = stats.spearmanr(sdsmlist,wslist)
    print rho

SCTRow()
# getWTFIDF()