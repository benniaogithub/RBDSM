#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: wmTorm.py
@time: 2016/4/28 2:40
"""
from scipy.sparse.linalg import svds
import scipy.io as sio
import time
from scipy.sparse import hstack
import os

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    # arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist

def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def wmTorm():

        #保存成matlab可以读取的格式，{"A":A}前面的A表示在matlab中的名字，后面的A表示在python中名字
        # source = u"I:/数据/word11247relation30/file_word/file_word_matrix_mat/"
        # dest = u"I:/数据/word11247relation30/rel_matrix/rel_mat/"
        # source = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_"+str(refdim)+u"_TFIDF/file_word/file_word_mat/"
        # dest = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_matrix/rel_mat/"
        source = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/file_word_senna_dense/file_word_mat/"
        dest = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/file_word_senna_dense/rel_matrix/rel_mat/"
        if not os.path.exists(dest):
            os.makedirs(dest)
        rellist = getRelList()
        wordlist = getWordList()
        relMats = []
        relcount = 0
        timeCheckin=time.clock()
        for i in range(0,len(wordlist)):
            word = wordlist[i]
            wordMat = sio.loadmat(source+u"l_"+word)[word]
            # wordMat = sio.loadmat(source+u"l_"+w1)[word]


        # for file in os.listdir(source):
        #     word = file.split(".")[0]
        #     # print file
        #     print word
        #     wordMat = sio.loadmat(source+file)[word]
            if relcount == 0:
                nRow,nCol = wordMat.get_shape()
                relcount = nCol
            if(len(relMats) == 0):
                for i in range(0,relcount):
                    relMats.append(wordMat[:,i])
            else:
                for i in range(0,relcount):
                    relMats[i] = hstack([relMats[i],wordMat[:,i]],format="csc")
            print relMats[0].get_shape()
        for i in range(0,relcount):
            matName = rellist[i]
            sio.savemat(dest+"r_"+matName,{matName:relMats[i].transpose()},oned_as='column') #行大于列 按列存成一维数组

        print("cost %s seconds" % (time.clock()-timeCheckin))

# wmTorm(refdim=1000)
wmTorm()