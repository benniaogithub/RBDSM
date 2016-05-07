#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: combNotExist.py
@time: 2016/5/8 3:13
"""

def getWordList():
    rfile = open("../res/none.txt")
    wordList = []
    for line in rfile:
        word = line.strip("\n")
        if word.find("_")==-1:
            print(word)
            wordList.append(word)
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def combine():
    wordlist = getWordList()
    for line in open("../res/wordNotExist.txt"):
        word  = line.strip()
        if(word not in wordlist):
            wordlist.append(word)
    for line in open("../res/wordNotExist2.txt"):
        word  = line.strip()
        if(word not in wordlist):
            wordlist.append(word)
    wfile = open("../res/wordNotExist3.txt","w")
    wfile.writelines(item+'\n' for item in wordlist)

combine()