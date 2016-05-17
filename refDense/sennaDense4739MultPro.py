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
import multiprocessing
import time

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


delRefList = getdelRef()
chosedRef = getRefList()
WordEmbedding = getEmbedding.getEmbeddingMat_senna()
SennaList = getSennaList()
refmap = []
# count = 0

def getDelRefMap(lock,index):
     count = 0
     for i in range(index,index*30000):
        word1 = delRefList[i]
     # for word1 in delRefList:
        # print(count)
        # count += 1

        print(count)

        if word1 not in SennaList:
            continue
        lock.acquire()
        w1vec = WordEmbedding[SennaList.index(word1),:]
        lock.release()
        sim = []
        for word2 in chosedRef:
            if word2 not in SennaList:
                sim.append(0)
                continue
            lock.acquire()
            w2vec = WordEmbedding[SennaList.index(word2),:]
            lock.release()
            sim.append(vecSim(w1vec,w2vec))
        chosed = chosedRef[np.argmax(sim)]

        item = word1+"\t"+chosed
        print(item)
        refmap.append(item)
        count += 1
        # print(refmap)
        # break
     wfile =  open("res/sennaMap_4739.txt","w")
     wfile.writelines(item+'\n' for item in refmap)

def master():
    for i in range(0,10):
        lock = multiprocessing.Lock()
        p = multiprocessing.Process(target = getDelRefMap, args=(lock,i))
        time.sleep(10)
        p.start()

def Out_of_order():
    delDef = getdelRef()
    x = range(0,381408)          #乱序
    # print(x)
    random.shuffle(x)
    newDelDef = []
    for i in range(0,381408):
        newDelDef.append(delDef[x[i]])

    wfile = open("res/DeleteRef_4739_2.txt","w")
    wfile.writelines(item+'\n' for item in newDelDef)

# Out_of_order()
# getDelRefMap()
master()