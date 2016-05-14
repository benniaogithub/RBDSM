#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: getWordList.py
@time: 2016/5/11 14:33
"""

def getWordList_12585():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))

    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def getWordList_senna():
    rfile = open(u"I:/实验/senna/senna/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList
