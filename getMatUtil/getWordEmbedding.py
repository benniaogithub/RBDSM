#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: getWordEmbedding.py
@time: 2016/5/14 16:08
"""
import numpy as np
import scipy.io as sio
import re

def creEmbeddingMat_senna():
    rfile = open(u"I:/数据/embedings/senna/embeddings.txt")
    embeddingMat = np.zeros([130000,50],dtype=np.float64)
    print(embeddingMat.shape)
    lines = rfile.readlines()
    rfile.close()
    print(len(lines))
    for i in range(0,len(lines)):
        line = lines[i]
        embedding = line.strip("\n").split(" ")
        for j in range(0,len(embedding)):
            embeddingMat[i][j]=embedding[j]
    sio.savemat(u"I:/数据/embedings/senna/embedding.mat",{"embedding":embeddingMat})

def getEmbeddingMat_senna():
    embeddingMat = sio.loadmat(u"I:/数据/embedings/senna/embedding.mat")["embedding"]
    return embeddingMat


def creEmbeddingMat_HLBL():
    rfile = open(u"I:/数据/embedings/hlbl/hlbl_reps_clean_2.50d.rcv1.clean.tokenized-CoNLL03.case-intact.txt")
    embeddingMat = np.zeros([246122,50],dtype=np.float64)
    wordList = []
    # print(embeddingMat.shape)
    lines = rfile.readlines()
    rfile.close()
    print(len(lines))
    for i in range(0,len(lines)):
        line = lines[i]
        sp_index=line.index(" ")
        # print line
        word = line[0:sp_index].strip().lower()
        # print(word)
        wordList.append(word)
        print(len(wordList))
        while line[sp_index+1]==" ":
            sp_index+=1
        linelist=line[sp_index+1:].split()

        for j in range(len(linelist)):
            embeddingMat[i][j] = linelist[j]
    sio.savemat(u"I:/数据/embedings/hlbl/embedding.mat",{"embedding":embeddingMat})
    wfile = open(u"I:/数据/embedings/hlbl/words.txt","w")
    wfile.writelines(item+'\n' for item in wordList)
# creEmbeddingMat_HLBL()
def getEmbeddingMat_HLBL():
    embeddingMat = sio.loadmat(u"I:/数据/embedings/hlbl/embedding.mat")["embedding"]
    return embeddingMat