#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: getRelationList.py
@time: 2016/5/11 14:53
"""

def getWordPairExptList():
    rfile = open("res/RELATIONS_relations.txt")
    List = []
    for line in rfile:
        List.append(line.strip("\n"))

    rfile.close()
    # arr = np.array(wordList)
    return  List