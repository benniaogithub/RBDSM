#!/usr/bin/env python
# encoding: utf-8
"""
@author: yx@xy
@license: Apache Licence
@file: countReference.py
@time: 2016/4/11 0:54
"""
import os
# for root,dirs,files in os.walk(dir):
#     for file in files:
#         print os.path.join(root,file)
def refCount():
    refCountDic = {}
    all = 0
    root = U"I:/数据/word12585relation30/file_word"
    for file in os.listdir(root):
        print(file)
        for line in open(os.path.join(root,file)):
             reference = line.strip().split("\t")[0]
             count = int(line.strip().split("\t")[2])
             sum = refCountDic.get(reference,0)+count
             refCountDic[reference]=sum
             all = all+count
        print(all)
             # print(reference,count,sum)
            # print(len(line.strip().split("\t")))
    wfile=open("referenceCount.txt","w")
    sorteddic = sorted(refCountDic.items(), key=lambda d:d[1], reverse = True )
    for item in sorteddic:
        wfile.write(item[0]+"----"+str(item[1])+"\n")
    wfile.close()

def MaxCount():
    max = 0
    root = u"I:\\数据\\word11247relation30\\file_word\\file_word"
    for file in os.listdir(root):
        print(file)
        for line in open(os.path.join(root,file)):

             count = int(line.strip().split("\t")[2])
             if(count>max):
                 max = count
    print max

def eachWordRefCount():
    root = "I:/file_word/file_word/"
    dic = {}
    all = 0
    for file in os.listdir(root):
        lines =open(os.path.join(root,file)).readlines()
        count = len(lines)
        all = count+all
        dic[file]=count
    wfile=open("wordReferenceCount.txt","w")
    sorteddic = sorted(dic.items(), key=lambda d:d[1], reverse = True )
    for item in sorteddic:
        wfile.write(item[0]+"----"+str(item[1])+"\n")
    wfile.close()
# dic = {'a':3 , 'b':2 , 'c': 1}
# wfile=open("referenceCount.txt","w")
# sorteddic = sorted(dic.items(), key=lambda d:d[1], reverse = True )
# for item in sorteddic:
#     print item
#     wfile.write(item[0]+"----"+str(item[1])+"\n")
# wfile.close()
# # wfile=open("referenceCount.txt","w")

# eacheWordRefCount()
# refCount()