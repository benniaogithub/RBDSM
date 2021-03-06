# encoding: utf-8
import os
import numpy as np
import scipy.io as sio
from scipy.sparse import csc_matrix
# from scipy.sparse import vstack
# from svd import svds12585 as svds
# from matTrans import wmTorm12585 as wmTorm

# def getreflist():
#     count=0
#     reflist = []
#     for line in open("../res/referenceCount.txt"):
#         if count==5000:break
#         reflist.append(line.split("----")[0])
#         count+=1
#     # arr = np.array(reflist)
#     # sio.savemat("reflist.mat",{"reflist":arr},oned_as='row')
#     # # np.save("../res/reflist.npy",arr)
#     return reflist
#
# def getrellist(filename):
#     rellist=[]
#     for line in open(filename):
#         rellist.append(line.strip("\n"))
#     arr = np.array(rellist)
#     sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
#     # np.save("../res/rellist.npy",arr)   #npy可不加
#     return rellist

def getreflist():
    rellist=[]
    for line in open("../res/ref_eachRel_800_6830.txt"):
        rellist.append(line.strip("\n"))
    return rellist

def getDenseMap():
    denseMap = {}
    for line in open("../res/wordnetMap_6830_synset.txt"):
        word1 = line.strip().split("\t")[0]
        word2 = line.strip().split("\t")[1]
        denseMap[word1] = word2
    return denseMap

def getrellist():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))

    return rellist

def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

denseMap = getDenseMap()

def getmatrixfile(sourcefile,word,destfile,reflist,rellist):
    result = np.zeros( (len(reflist),len(rellist)))
    # print(denseMap)
    for line in open(sourcefile):
        linelist=line.strip("\n").split("\t")
        if linelist[1] in rellist:
            if linelist[0] in reflist:
                result[reflist.index(linelist[0]),rellist.index(linelist[1])] += int(linelist[2])
            elif linelist[0] in denseMap.keys():
                result[reflist.index(denseMap[linelist[0]]),rellist.index(linelist[1])] += int(linelist[2])
        # if linelist[0] in reflist and linelist[1] in rellist:

    # wfile=open(destfile,"w")
    cscResult = csc_matrix(result)
    sio.savemat(destfile,{word:cscResult},oned_as='column')#因为con.mat不能直接保存，所以保留后缀txt
    # np.save(destfile,result)
#
def getWordMat():
    source = u"I:/数据/word12585relation30/file_word/"
    dest = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/file_word_senna_dense/file_word_mat/"
    # reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
    # rellist=getrellist(u"I:/数据/statistic/relations.txt")
    if not os.path.exists(dest):
        os.makedirs(dest)
    reflist=getreflist()
    rellist=getrellist()
    for file in os.listdir(source):
        # reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
        # rellist=getrellist(u"I:/数据/statistic/relations.txt")
        word = file.split(".") [0]
        print word
        getmatrixfile(source+file,word,dest+u"l_"+word,reflist,rellist)


# def test():
#     source = u"I:/数据/word11247relation30/file_word/file_word/"
#     dest = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
#     reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
#     rellist=getrellist(u"I:/数据/statistic/relations.txt")
#     getmatrixfile(source+"con.txt",dest+"con.txt".strip(".txt")  ,reflist,rellist)

# test()
getWordMat()
# wmTorm.wmTorm()
# svds.SVDs()
# getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")


