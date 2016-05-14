#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: TOEFLTest.py
@time: 2016/4/28 3:53
"""
import wordPairSim12585wTFIDFCol as wordPairSim
import numpy as np
from getMatUtil import getWordEmbedding as getEmbedding

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

def getWordList():
    rfile = open(u"I:/数据/embedings/hlbl/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

WordEmbedding = getEmbedding.getEmbeddingMat_HLBL()

count = 0
total = 0
wordList = getWordList()
for line in open("../res/TOEFL.txt"):
    word = line.strip().split("\t")[0]
    choices = line.strip().split("\t")[1]
    choice1 = choices.split(",")[0]
    choice2 = choices.split(",")[1]
    choice3 = choices.split(",")[2]
    choice4 = choices.split(",")[3]
    if word not in wordList:
        # print count
        # print word
        continue
    if choice1 not in wordList:
        # print count
        # print choice1
        continue
    if choice2 not in wordList:
        # print count
        # print choice2
        continue
    if choice3 not in wordList:
        # print count
        # print choice3
        continue
    if choice4 not in wordList:
        # print count
        # print choice4
        continue
    total += 1
    chosen = np.argmax([vecSim(WordEmbedding[wordList.index(word),:],WordEmbedding[wordList.index(choice1),:]),vecSim(WordEmbedding[wordList.index(word),:],WordEmbedding[wordList.index(choice2),:]),vecSim(WordEmbedding[wordList.index(word),:],WordEmbedding[wordList.index(choice3),:]),vecSim(WordEmbedding[wordList.index(word),:],WordEmbedding[wordList.index(choice4),:])])
    print(chosen)
    if(chosen == 0):
        count += 1
print(count)
print(total)
print(float(count)/total)
