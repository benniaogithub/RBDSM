#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: TOEFLTest.py
@time: 2016/4/28 3:53
"""
import wordPairSim12585 as wordPairSim
import numpy as np
def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

count = 0
wordList = getWordList()
for line in open("../res/TOEFL.txt"):
    word = line.strip().split("\t")[0]
    choices = line.strip().split("\t")[1]
    choice1 = choices.split(",")[0]
    choice2 = choices.split(",")[1]
    choice3 = choices.split(",")[2]
    choice4 = choices.split(",")[3]
    if word not in wordList:
        count += 1
        # print count
        # print word
        continue
    if choice1 not in wordList:
        count += 1
        # print count
        # print choice1
        continue
    if choice2 not in wordList:
        count += 1
        # print count
        # print choice2
        continue
    if choice3 not in wordList:
        count += 1
        # print count
        # print choice3
        continue
    if choice4 not in wordList:
        count += 1
        # print count
        # print choice4
        continue
    print np.argmax([wordPairSim.wordlantCosSim(word,choice1),wordPairSim.wordlantCosSim(word,choice2),wordPairSim.wordlantCosSim(word,choice3),wordPairSim.wordlantCosSim(word,choice4)])

