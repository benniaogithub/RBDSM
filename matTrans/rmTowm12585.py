#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: rmTowm.py
@time: 2016/4/25 14:51
"""

import scipy.io as sio
import time
import os
from scipy import hstack
from scipy import vstack

import numpy as np

def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    arr = np.array(wordList)
    # print arr
    # sio.savemat("wordlist.mat",{"wordlist":arr},oned_as='row')

    return  wordList

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist

# def rmTowmByGroup():       #一次将所有转成所有单词的mat 内存不够
#     source = u"I:/数据/word11247relation30/rel_matrix/rel_mat_latent_500/"
#     dest = u"I:/数据/word11247relation30/file_word/word_mat_latent_500/"
#     wordlist = getWordList()
#     times = 3
#     groupSize = int(len(wordlist)/times)+1     #每次处理多单词
#     count = 0
#     for t in range(0,3):
#         startWordIndex = t*groupSize
#         endWordIndex = min(groupSize*(t+1),len(wordlist))
#         print "start"
#         print startWordIndex
#         print endWordIndex
#         wordMats = {}
#         timeCheckin = time.clock()
#         for file in os.listdir(source):
#             rel = file.split(".")[0].split("_")[1]
#             # print file
#             print rel
#             relMat = sio.loadmat(source+file)[rel]
#             if(len(wordMats) == 0):
#                 for i in range(startWordIndex ,endWordIndex):
#
#                     wordMats["word_"+str(i)] = relMat[i,:]
#                     # print wordMats[wordlist[i]].shape
#                 print len(wordMats)
#             else:
#                 for i in range(startWordIndex ,endWordIndex):
#                     wordMats["word_"+str(i)] = vstack([wordMats["word_"+str(i)],relMat[i,:]])
#                     # print wordMats[wordlist[i]].shape
#                     # if(wordMats["word_"+str(i)].shape[0])>30:
#                     #      print "FFFFFFFFFFFF"
#         count = count+len(wordMats)
#         print count
#         for key in wordMats.keys():
#             wordName = wordlist[int(key.split("_")[1])]
#             sio.savemat(dest+"l_"+wordName,{wordName:wordMats[key]})
#             # print wordMats[key].shape
#         print("cost %s seconds" % (time.clock()-timeCheckin))

def rmTowmByGrouplus(dim = 500):       #一次将所有转成所有单词的mat 内存不够
    # source = u"I:/数据/word11247relation30/rel_matrix/rel_mat_latent_"
    # dest = u"I:/数据/word11247relation30/file_word/word_mat_latent_"
    # source = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/rel_matrix_lus/rel_mat_latent_"
    # dest = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/file_word_lus/word_matus_latent_"
    source = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/file_word_senna_dense/rel_spc/rel_matrix_"
    dest =  u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/file_word_senna_dense/rel_spc/word_matrix_"
    # source = u"I:/数据/word11247relation30/test/rel_mat_latent_"
    # dest = u"I:/数据/word11247relation30/test/word_matus_latent_"
    source = source+str(dim)+u"/"
    dest = dest+str(dim)+u"/"
    if not os.path.exists(dest):
            os.makedirs(dest)
    wordlist = getWordList()
    rellist = getRelList()
    times = 3
    groupSize = int(len(wordlist)/times)+1     #每次处理多单词
    count = 0
    for t in range(0,times):
        startWordIndex = t*groupSize
        endWordIndex = min(groupSize*(t+1),len(wordlist))
        wordMats = {}
        timeCheckin = time.clock()
        for i in range(0,len(rellist)):
            relName = rellist[i]
            relMat = sio.loadmat(source+"r_"+relName+".mat")["spcRelmat"]

            if(len(wordMats) == 0):
                print endWordIndex
                for i in range(startWordIndex ,endWordIndex):
                    wordMats[wordlist[i]] = relMat[i,:]
            else:
                for i in range(startWordIndex ,endWordIndex):
                    wordMats[wordlist[i]] = vstack([wordMats[wordlist[i]],relMat[i,:]])
        for key in wordMats.keys():
            sio.savemat(dest+"l_"+key,{key:wordMats[key]})
        print("cost %s seconds" % (time.clock()-timeCheckin))



# rmTowm()
# rmTowmByGroup(100)
# rmTowmByGroup(500)
# rmTowmByGroup(800)
# rmTowmByGroup(1000)
# rmTowmByGroup(1200)
rmTowmByGrouplus(256)
# rmTowmByGroup(250)
# rmTowmByGroup(400)
# rmTowmByGroupOrig()
# rmTowmByGroup()
#rmTowmAll()
# rmTowmByGroup(refdim=1500,dim = 300)
# rmTowmByGroup(refdim=1500,dim = 250)