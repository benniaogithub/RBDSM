#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence
@file: choseByTFIDF.py
@time: 2016/4/27 22:07
"""
import os

wordlist={}
wfile=open("vocabADD.txt","w")
for file in os.listdir(u"I:\\数据\\corpus\\fileWordAdd"):
	wordlist[file[0:-4]]=1
	wfile.write(file[0:-4]+"\n")
print len(wordlist)
wfile.close()
	