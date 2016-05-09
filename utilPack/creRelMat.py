#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: creRelMat.py
@time: 2016/5/9 3:17
"""
import numpy as np
import scipy.io as sio

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    arr = np.array(rellist)
    sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist
getRelList()