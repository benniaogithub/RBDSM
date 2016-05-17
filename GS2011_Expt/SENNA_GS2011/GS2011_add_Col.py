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
from getMatUtil import getWordEmbedding as getEmbedding

def getWTFIDF():
    wArr = sio.loadmat(u"I:/数据/word12585relation30/weight/wTFIDF2.mat")["wTFIDF"][0]
    # print(wArr)
    # arr = np.array(wordList)
    return  wArr

# def getWordPairVec(w1,w2):
#      # root =  u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"
#      wordList = getWordList()
#      WordEmbedding = getEmbedding.getEmbeddingMat_HLBL()
#      w1vec = WordEmbedding[wordList.index(w1),:]
#      w2vec = WordEmbedding[wordList.index(w2),:]
#      vec = hstack([w1vec,w2vec])
#      return vec

def creSampStep_1():              #提取前三列 其他不要了
    wordList = getWordList()
    rfile = open("../res/GS2011data.txt")
    sampleList = []
    for line in rfile:
        item = line.strip("\n").split(" ")
        if item[1] in wordList and item[2] in wordList and  item[3] in wordList and item[4]:
            sampleList.append(line)
    rfile.close()
    wfile = open(u"res/GS2011_SENNA.txt","w")
    wfile.writelines(item for item in sampleList)


def getWordList():
    rfile = open(u"I:/数据/embedings/senna/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

WordEmbedding = getEmbedding.getEmbeddingMat_senna()
wordList = getWordList()
def sentCombMat_add(w1,w2,w3):

    w1Mat = WordEmbedding[wordList.index(w1),:]
    w2Mat = WordEmbedding[wordList.index(w1),:]
    w3Mat = WordEmbedding[wordList.index(w1),:]

    return w1Mat+w2Mat+w3Mat



def vecSim(x, y):

    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):
        # print "fdddd"
        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim


     # for i in range(0,np.shape(w1Mat)[1]):         #单词按参考词的条件概率   一列一列算相似度
     #    sim = vecSim(w1Mat[:,i],w2Mat[:,i])+sim
     #    # print sim/np.shape(w1Mat)[1]
     # return sim/np.shape(w1Mat)[1]
def GS2011_add_Col():        #三个词组成的句子，向量相加 ,计算相似度按行

    wslist = []
    sdsmlist = []
    count = 1

    for line in open(u"res/GS2011_SENNA.txt"):
        item = line.strip("\n").split(" ")
        w11 = item[1]
        w12 = item[2]
        w13 = item[3]
        w21 = item[4]
        sim1 = vecSim(sentCombMat_add(w11,w12,w13),sentCombMat_add(w21,w12,w13))
        sim2 = item[5]
        wslist.append(sim1)
        sdsmlist.append(sim2)
        print count
        count += 1
    rho, pval = stats.spearmanr(sdsmlist,wslist)
    print rho
GS2011_add_Col()
# creSampStep_1()
# getWTFIDF()