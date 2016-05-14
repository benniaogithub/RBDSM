#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: prePairRelFile.py
@time: 2016/5/11 14:28
"""
from getMatUtil import getWordList
from getMatUtil import getRelationList
import random
from scipy import hstack
from scipy import vstack
import numpy as np
import scipy.io as sio

def getWordPairVec(w1,w2):
     # root =  u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"

     root = u"I:/数据/word12585relation30/rel_30_ref_5000/rel_svd/file_word_lus/word_mat_latent_300/"
     #
     # w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     # w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     vec = w1Mat[0,:]
     vec = hstack([vec,w2Mat[0,:]])
     # print np.shape(w1Mat)[1]
     for i in range(1,np.shape(w1Mat)[0]):         #单词按参考词的条件概率   一列一列算相似度
        vec = hstack([vec,w1Mat[i,:]])
        vec = hstack([vec,w2Mat[i,:]])
        # print np.shape(vec)
     return vec

def getWTFIDF():
    wArr = sio.loadmat(u"I:/数据/word12585relation30/weight/wTFIDF2.mat")["wTFIDF"][0]
    # print(wArr)
    # arr = np.array(wordList)
    return  wArr
wArr = getWTFIDF()

def vecSimCol(x, y):
    # result1 = x.T.dot(y)
    # result1 =  result1.tolist()[0][0]           #svd 之前的稀疏原始矩阵用这个
    x = x*wArr
    y = y*wArr
    result1 = np.dot(x,y)
    result2 = np.linalg.norm(x)
    result3 = np.linalg.norm(y)
    if(result2*result3 == 0):
        # print "fdddd"
        return 1
    cos = result1/(result2*result3)
    sim = 0.5+0.5*cos
    return sim


def getWordPairSimVec(w1,w2):
     # root =  u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_spc/spc_1_350/word_matrix/"

     root = u"I:/数据/word12585relation30/rel_30_ref_5000/rel_svd/file_word_lus/word_mat_latent_300/"
     w1Mat = sio.loadmat(root+u"l_"+w1)[w1]
     w2Mat = sio.loadmat(root+u"l_"+w2)[w2]
     vec = np.zeros(np.shape(w1Mat)[1])

     # for i in range(0,np.shape(w1Mat)[0]):         #单词按参考词的条件概率   一列一列算相似度
     #    sim = vecSim(w1Mat[i,:],w2Mat[i,:])+sim
     #    # print sim/np.shape(w1Mat)[1]
     # return sim/np.shape(w1Mat)[0]
     for i in range(0,np.shape(w1Mat)[1]):         #单词按参考词的条件概率   一列一列算相似度
        sim = vecSimCol(w1Mat[:,i],w2Mat[:,i])
        vec[i] = sim
        # print sim/np.shape(w1Mat)[1]
     return vec


def creSampStep_1():              #提取前三列 其他不要了
    wordList = getWordList.getWordList_12585()
    rfile = open("res/RELATIONSRaw.txt")
    sampleList = []
    relations = []
    for line in rfile:
        # wordList.append()
        item = line.strip("\n").split("\t")
        print(item)
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
    wfile = open("res/RELATIONS_step_01.txt","w")
    wfile.writelines(item+'\n' for item in sampleList)
    wfile2 = open("res/RELATIONS_relations.txt","w")
    wfile2.writelines(item+'\n' for item in relations)

def creSampStep_2():
    relList = getRelationList.getWordPairExptList()
    rfile = open("res/RELATIONS_step_01.txt")
    sampleList = []
    sampleTrain = []
    TrainLable = []
    sampleTest = []
    testLable = []
    for line in rfile:
        sampleList.append(line.strip("\n"))
    rfile.close()

    x = range(0,7267)          #乱序
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

    for i in range(6000,7267):
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

    wfile = open("res/RELATIONS_train.txt","w")
    wfile.writelines(item+'\n' for item in sampleTrain)
    wfile2 = open("res/RELATIONS_test.txt","w")
    wfile2.writelines(item+'\n' for item in sampleTest)
    wfile3 = open("res/RELATIONS_trainLable.txt","w")
    wfile3.writelines(str(item)+'\n' for item in TrainLable)
    wfile4 = open("res/RELATIONS_testLable.txt","w")
    wfile4.writelines(str(item)+'\n' for item in testLable)
    # arr = np.array(wordList)
def creSimVecSamp():
    lines = open("res/RELATIONS_train.txt").readlines()
    line = lines[0]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairSimVec(word1,word2)
    Mat = wordvec
    for i in range(1,len(lines)):
        line = lines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairSimVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat("res/PairRelSimTrain.mat",{"train":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    lines = open("res/RELATIONS_test.txt").readlines()
    line = lines[0]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairSimVec(word1,word2)           #300维度的相似度
    Mat = wordvec
    for i in range(1,len(lines)):
        line = lines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairSimVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat("res/PairRelTestSim.mat",{"tests":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
    # print(trainMat[])

    lines = open("res/RELATIONS_trainLable.txt").readlines()
    list = []
    for line in lines:
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat("res/PairRelSimTrainLable.mat",{"trainLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    lines = open("res/RELATIONS_testLable.txt").readlines()
    list = []
    for line in lines:
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat("res/PairRelSimTestLable.mat",{"testLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

def creAllvecSamp():
    Tlines = open("res/RELATIONS_train.txt").readlines()
    TLlines = open("res/RELATIONS_trainLable.txt").readlines()
    batchNum = 10
    batchSize = len(Tlines)/10
    for b in range(0,batchNum):
        line = Tlines[b*batchSize]
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairVec(word1,word2)
        Mat = wordvec

        for i in range(b*batchSize+1,(b+1)*batchSize):
            line = Tlines[i]
            print(i)
            word1 = line.strip("\n").split("\t")[0]
            word2 = line.strip("\n").split("\t")[1]
            wordvec = getWordPairVec(word1,word2)
            Mat =  vstack([Mat,wordvec])
            print(Mat.shape)
        sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelSimTrain_"+str(b)+".mat",{"train":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组


        list = []
        for i in range(b*batchSize,(b+1)*batchSize):
            line = TLlines[i]
            list.append(int(line.strip()))
            Mat = np.array(list)
            sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelSimTrainLable_"+str(b)+".mat",{"trainLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    Telines = open("res/RELATIONS_test.txt").readlines()
    line = Telines[0]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairVec(word1,word2)           #300维度的相似度
    Mat = wordvec
    for i in range(1,600):
        line = Telines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelTestSim_0.mat",{"tests":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
    # print(trainMat[])
    line = Telines[600]
    word1 = line.strip("\n").split("\t")[0]
    word2 = line.strip("\n").split("\t")[1]
    wordvec = getWordPairVec(word1,word2)           #300维度的相似度
    Mat = wordvec
    for i in range(601,len(Telines)):
        line = Telines[i]
        print(i)
        word1 = line.strip("\n").split("\t")[0]
        word2 = line.strip("\n").split("\t")[1]
        wordvec = getWordPairVec(word1,word2)
        Mat =  vstack([Mat,wordvec])
        print(Mat.shape)
    sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelTestSim_1",{"tests":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组
    # print(trainMat[])

    lines = open("res/RELATIONS_testLable.txt").readlines()
    list = []
    for i in range(0,600):
        line = lines[i]
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelSimTestLable_0.mat",{"testLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组

    list = []
    for i in range(600,len(lines)):
        line = lines[i]
        list.append(int(line.strip()))
    Mat = np.array(list)
    sio.savemat(u"I:/数据/wordpairRelExpt/allVec/PairRelSimTestLable_1.mat",{"testLable":Mat.transpose()},oned_as='column') #行大于列 按列存成一维数组



    # arr = np.array(wordList)
# getWordPairVec("eat","food")
# creSampStep_3()
# creAllvecSamp()
creSimVecSamp()