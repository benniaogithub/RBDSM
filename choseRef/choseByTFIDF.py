#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: choseByTFIDF.py
@time: 2016/4/27 22:07
"""
import scipy.io as sio
import numpy as np
from scipy import hstack
from scipy import vstack
import  os

def getRefList():
    reflist=[]
    for line in open("../res/ref.txt"):
        reflist.append(line.strip("\n"))
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return reflist

def everyRelMaxTFIDF(dim=1000):
    relpath = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/statistic/TFIDF_result.mat"
    dest  = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/statistic/"
    if not os.path.exists(dest):
        os.makedirs(dest)
    relmat = sio.loadmat(relpath)["result"]
    refList = getRefList()
    chosedRefIndexArr = None
    chosedRefArr = None
    refArr = np.array(refList)
    for row in relmat:
        sortIndex = np.argsort(row)[0-dim:]
        if chosedRefArr == None:
            chosedRefArr = refArr[sortIndex]
        else:
            chosedRefArr = vstack([chosedRefArr,refArr[sortIndex]])

        if chosedRefIndexArr == None:
            chosedRefIndexArr = sortIndex
        else:
            chosedRefIndexArr = hstack([chosedRefIndexArr,sortIndex])
    print chosedRefIndexArr.shape
    refArr = refArr[np.unique(chosedRefIndexArr)]
    print refArr.shape[0]
    wfile = open("../res/ref_eachRel_"+str(dim)+"_"+str(refArr.shape[0])+".txt","w")
    wfile.writelines(str(item)+'\n' for item in refArr.flat)
    sio.savemat(dest+"TFIDF_chosedRef_"+str(dim)+"_"+str(refArr.shape[0])+".mat",{"chosedRef_"+str(dim):chosedRefArr})

# everyRelMaxTFIDF(1000)
# everyRelMaxTFIDF(1500)
# b = np.arange(6)
# wfile = open("../res/ref_eachRel_300.txt","w")
# wfile.writelines(str(item)+'\n' for item in b.flat)
# b[1] = 5
# a = np.argsort(b)[0-3:]
# c = hstack([a,b])
#
#
# print c
# print a
# print b
# print b[a][-3:]