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

def getAllReft():
    rfile = open(u"../res/ref.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getRefList():
    rfile = open(u"../res/ref_eachRel_500_4739.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getSennaList():
    rfile = open(u"I:/数据/embedings/senna/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getdelRef():
    rfile = open("res/DeleteRef_4739.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getDelRefList():
    delRefList = []
    allRef = getAllReft()
    chosedRef = getRefList()
    for ref in allRef:
        if ref not in chosedRef:
            print(ref)
            delRefList.append(ref)
    wfile = open("res/DeleteRef_4739.txt","w")
    wfile.writelines(item+'\n' for item in delRefList)

def vecSim(x, y):
    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):

        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim

def getDelRefMap():
     delRefList = getdelRef()
     chosedRef = getRefList()
     WordEmbedding = getEmbedding.getEmbeddingMat_senna()
     SennaList = getSennaList()
     map = []
     for word1 in delRefList:
        if word1 not in SennaList:
            continue
        w1vec = WordEmbedding[SennaList.index(word1),:]
        sim = []
        for word2 in chosedRef:
            if word2 not in SennaList:
                sim.append(0)
                continue
            w2vec = WordEmbedding[SennaList.index(word2),:]
            sim.append(vecSim(w1vec,w2vec))
        chosed = chosedRef[np.argmax(sim)]
        print(word1+"\t"+chosed)
        map.append(word1+"\t"+chosed)
     wfile =  open("res/sennaMap6830.txt","w")
     wfile.writelines(item+'\n' for item in map)



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

# def creVecSamp():
#     lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_train.txt").readlines()
#     line = lines[0]
#     word1 = line.strip("\n").split("\t")[0]
#     word2 = line.strip("\n").split("\t")[1]
#     wordvec = getWordPairVec(word1,word2)
#     Mat = wordvec
#     for i in range(1,len(lines)):
#         line = lines[i]
#         print(i)
#         word1 = line.strip("\n").split("\t")[0]
#         word2 = line.strip("\n").split("\t")[1]
#         wordvec = getWordPairVec(word1,word2)
#         Mat =  vstack([Mat,wordvec])
#         print(Mat.shape)
#     sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTrain.mat",{"train":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
#
#     lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_test.txt").readlines()
#     line = lines[0]
#     word1 = line.strip("\n").split("\t")[0]
#     word2 = line.strip("\n").split("\t")[1]
#     wordvec = getWordPairVec(word1,word2)           #300维度的相似度
#     Mat = wordvec
#     for i in range(1,len(lines)):
#         line = lines[i]
#         print(i)
#         word1 = line.strip("\n").split("\t")[0]
#         word2 = line.strip("\n").split("\t")[1]
#         wordvec = getWordPairVec(word1,word2)
#         Mat =  vstack([Mat,wordvec])
#         print(Mat.shape)
#     sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelTestSim.mat",{"tests":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
#     # print(trainMat[])
#
#     lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_trainLable.txt").readlines()
#     list = []
#     for line in lines:
#         list.append(int(line.strip()))
#     Mat = np.array(list)
#     sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTrainLable.mat",{"trainLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
#
#     lines = open(u"I:/数据/wordpairRelExpt/HLBL/RELATIONS_testLable.txt").readlines()
#     list = []
#     for line in lines:
#         list.append(int(line.strip()))
#     Mat = np.array(list)
#     sio.savemat(u"I:/数据/wordpairRelExpt/HLBL/PairRelSimTestLable.mat",{"testLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
# getDelRefList()
getDelRefMap()