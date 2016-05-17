#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: sennaExist.py
@time: 2016/5/16 3:55
"""

def getSennaWordList():
    rfile = open(u"I:/数据/embedings/senna/words.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()

    return  wordList

def getRefList():
    rfile = open(u"../res/ref_eachRel_500_4739.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

wordList = getWordList()
sennalist = getSennaWordList()
reflist = getRefList()
refnot = []
wordnot = []

for word in wordList:
    if  word in sennalist:
        wordnot.append(word)

for word in reflist:
    if  word  in sennalist:
        refnot.append(word)


wfile = open(u"res/SennaExistword.txt","w")
wfile.writelines(item+"\n" for item in wordnot)
wfile = open(u"res/SennaExistref.txt","w")
wfile.writelines(item+"\n" for item in refnot)