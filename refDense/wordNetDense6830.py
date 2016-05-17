#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: test.py
@time: 2016/5/15 13:56
"""
from nltk.corpus import wordnet as wn
import random


def getdelRef():
    rfile = open("res/DeleteRef_6830_2.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def getRefList():
    rfile = open(u"../res/ref_eachRel_800_6830.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    return  wordList

def Out_of_order():
    delDef = getdelRef()
    x = range(0,379317)          #乱序
    # print(x)
    random.shuffle(x)
    newDelDef = []
    for i in range(0,379317):
        newDelDef.append(delDef[x[i]])

    wfile = open("res/DeleteRef_6830_2.txt","w")
    wfile.writelines(item+'\n' for item in newDelDef)

def getDelRefMapSyn():

     delRefList = getdelRef()
     # print delRefList
     chosedRef = getRefList()
     refmap =[]
     for i in range(0,len(delRefList)):
        word1 = delRefList[i]
        print(i)
        wordSynset = wn.synsets(word1)
        if not len(wordSynset) == 0:
            # print(wordSynset)
            chosed = False
            que = []
            pop = -1
            push = -1
            for i in range(len(wordSynset)):
                que.append(wordSynset[i])
                push += 1
            while not chosed and pop < push :
                # print("_________"+str(len(que)))
                pop += 1
                word2 = que[pop].name().split(".")[0]
                print("------------"+word2)
                if(word2 in chosedRef):
                    item = word1+"\t"+word2
                    print(item)
                    chosed = True
                    refmap.append(item)
                    break
                wordSynset = que[pop].hypernyms()
                for i in range(len(wordSynset)):
                    que.append(wordSynset[i])
                    push += 1
     wfile =  open("res/wordnetMap_6830_synset.txt","w")
     wfile.writelines(item+'\n' for item in refmap)
# Out_of_order()

getDelRefMapSyn()