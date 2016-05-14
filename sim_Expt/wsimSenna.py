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
from getMatUtil import getWordEmbedding as getEmbedding
np.set_printoptions(threshold='nan')



def getWordList():
    rfile = open(u"I:/实验/senna/senna/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

WordEmbedding = getEmbedding.getEmbeddingMat_senna()
wordList = getWordList()
print len(wordList)
# print(wordList[1])
def vecSim(x, y):
    # result1 = x.T.dot(y)
    # result1 =  result1.tolist()[0][0]           #svd 之前的稀疏原始矩阵用这个
    # x = x*wArr
    # y = y*wArr
    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):
        # print "fdddd"
        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim


def wordCosSim(w1,w2):
     # root=u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_svd/file_word_lus/word_matus_latent_324/"
     # root = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_svd/file_word_lus/word_mat_latent_324/"
     # root = u"I:/数据/word12585relation30/rel_30_ref_5000/rel_svd/file_word_lus/word_mat_latent_350/"
     #
     # w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     # w2Mat = sio.loadmat(root+u"l_"+w2)[w2]

     # for i in range(0,np.shape(w1Mat)[0]):         #单词按参考词的条件概率   一列一列算相似度
     #    sim = vecSim(w1Mat[i,:],w2Mat[i,:])+sim
     #    # print sim/np.shape(w1Mat)[1]
     # return sim/np.shape(w1Mat)[0]

     # print WordEmbedding[1,:]
              #单词按参考词的条件概率   一列一列算相似度
     sim = vecSim(WordEmbedding[wordList.index(w1),:],WordEmbedding[wordList.index(w2),:])
        # print sim/np.shape(w1Mat)[1]
     return sim

def SCTCol():

    wslist = []
    sdsmlist = []
    count = 1

    for line in open("../res/WS-353.txt"):
        w1 = line.split("\t")[0]
        w2 = line.split("\t")[1]
        if w1 in wordList and w2 in wordList:
            sim1 = wordCosSim(w1,w2)
            sim2 = line.strip("\n").split("\t")[-1]
            print sim2
            wslist.append(sim1)
            sdsmlist.append(sim2)
            print count
            count += 1
    rho, pval = stats.spearmanr(sdsmlist,wslist)
    print rho



SCTCol()

# getWTFIDF()