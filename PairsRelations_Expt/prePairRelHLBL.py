#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: prePairRelFile.py
@time: 2016/5/11 14:28
"""
from getMatUtil import getRelationList
from scipy import hstack
from scipy import vstack
import numpy as np
import scipy.io as sio
from getMatUtil import getWordEmbedding as getEmbedding
import random

def getWordList():
    rfile = open(u"I:/数据/embedings/HLBL/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def getWordPairVec(w1,w2):
     # root =  u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"
     wordList = getWordList()
     WordEmbedding = getEmbedding.getEmbeddingMat_HLBL()
     w1vec = WordEmbedding[wordList.index(w1),:]
     w2vec = WordEmbedding[wordList.index(w2),:]
     vec = hstack([w1vec,w2vec])


     return vec

def creSampStep_1():              #提取前三列 其他不要了
    wordList = getWordList()
    rfile = open("res/RELATIONSRaw.txt")
    sampleList = []
    relations = []
    for line in rfile:
        # wordList.append()
        item = line.strip("\n").split("\t")
        # print(item)
        word1 = item[0].lower()
        word2 = item[2].lower()
        relation = item[1]
        if(word1 in wordList and word2 in wordList):
            sample = word1+"\t"+word2+"\t"+relation
            sampleList.append(sample)
            print(sample)
            if(relation not in relations):
                relations.append(relation)
    rfile.close()
    wfile = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_step_01.txt","w")
    wfile.writelines(item+'\n' for item in sampleList)
    wfile2 = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_relations.txt","w")
    wfile2.writelines(item+'\n' for item in relations)

def creSampStep_2():
    relList = getRelationList.getWordPairExptList()
    rfile = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_step_01.txt")
    sampleList = []
    sampleTrain = []
    TrainLable = []
    sampleTest = []
    testLable = []
    for line in rfile:
        sampleList.append(line.strip("\n"))
    rfile.close()

    x = range(0,7248)          #乱序
    print(x)
    random.shuffle(x)

    for i in range(0,6000):
        item = sampleList[x[i]].split("\t")
        print(item)
        word1 = item[0]
        word2 = item[1]
        relation = item[2]
        relationLable = relList.index(relation)+1
        print(relationLable)
        sample = word1+"\t"+word2
        sampleTrain.append(sample)
        TrainLable.append(relationLable)

    for i in range(6000,7248):
        item = sampleList[x[i]].split("\t")
        print(item)
        word1 = item[0]
        word2 = item[1]
        relation = item[2]
        relationLable = relList.index(relation)+1
        print(relationLable)
        sample = word1+"\t"+word2
        sampleTest.append(sample)
        testLable.append(relationLable)

    wfile = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_train.txt","w")
    wfile.writelines(item+'\n' for item in sampleTrain)
    wfile2 = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_test.txt","w")
    wfile2.writelines(item+'\n' for item in sampleTest)
    wfile3 = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_trainLable.txt","w")
    wfile3.writelines(str(item)+'\n' for item in TrainLable)
    wfile4 = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_testLable.txt","w")
    wfile4.writelines(str(item)+'\n' for item in testLable)

def creVecSamp():
    lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_train.txt").readlines()
    line = lines[0]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairVec(word1,word2)
    Mat = wordvec
    for i in range(1,len(lines)):
        line = lines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTrain.mat",{"train":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_test.txt").readlines()
    line = lines[0]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairVec(word1,word2)           #300维度的相似度
    Mat = wordvec
    for i in range(1,len(lines)):
        line = lines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelTestSim.mat",{"tests":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
    # print(trainMat[])

    lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_trainLable.txt").readlines()
    list = []
    for line in lines:
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTrainLable.mat",{"trainLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_testLable.txt").readlines()
    list = []
    for line in lines:
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTestLable.mat",{"testLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

# creSampStep_1()
creSampStep_2()
creVecSamp()