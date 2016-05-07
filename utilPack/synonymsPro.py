#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: word500ListPro.py
@time: 2016/5/8 0:24
"""
def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def preProcess():
    # wfile = open("../res/synonyms.txt","w")
    wordlist = getWordList()
    wordNotExist = []
    for line in open("../res/synonyms.txt"):
        word = line.strip().split(",")[0]
        # print(word)
        # print(len(line.split(",")))
        synonyms1 = line.strip().split(",")[1]
        synonyms2 = line.strip().split(",")[2]
        if not word in wordlist:
            wordNotExist.append(word)
        if not synonyms1 in wordlist:
            wordNotExist.append(synonyms1)
        if not synonyms2 in wordlist:
            wordNotExist.append(synonyms2)
    wfile = open("../res/wordNotExist2.txt","w")
    wfile.writelines(item+'\n' for item in wordNotExist)
preProcess()