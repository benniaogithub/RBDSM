# encoding: utf-8
import os
import numpy as np
import scipy.io as sio
from scipy.sparse import csc_matrix
from scipy.sparse import vstack
# def getreflist(filename):
#     count=0
#     reflist = []
#     for line in open(filename):
#         if count==5000:break
#         reflist.append(line.split("----")[0])
#         count+=1
#     arr = np.array(reflist)
#     sio.savemat("reflist.mat",{"reflist":arr},oned_as='row')
#     # np.save("../res/reflist.npy",arr)
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

def getrefMat():
    source = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/statistic/TFIDF_chosedRef_1500_11259.mat"
    refMat = sio.loadmat(source)["chosedRef_1500"]
    # print refMat[1][0]
    reflist = []
    for row in refMat:
        refline = []
        for ref in row:
            refline.append(str(ref).strip())
        reflist.append(refline)
        # print refline
    return reflist

def getrellist():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))

    return rellist

def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def getmatrixfile(sourcefile, word, destfile, refMat, rellist):          #生成的每个单词的表示是参考词——关系。后面的处理会转置
    result = np.zeros((len(refMat[0]),len(rellist)))
    for line in open(sourcefile):
        linelist=line.strip("\n").split("\t")
        rel = linelist[1]
        ref = linelist[0]
        # if linelist[0] in refMat and linelist[1] in rellist:
        #     result[refMat.index(linelist[0]), rellist.index(linelist[1])]=int(linelist[2])
        if  rel in rellist:

            ref_rel = refMat[rellist.index(rel)]
            # print ref_rel
            if(ref in ref_rel):
                result[ref_rel.index(ref)][rellist.index(rel)] = int(linelist[2])
    # wfile=open(destfile,"w")
    cscResult = csc_matrix(result)
    # print cscResult.shape
    sio.savemat(destfile,{word:cscResult},oned_as='column')        #因为con.mat不能直接保存，所以保留后缀txt
    # np.save(destfile,result)
#
def getWordMat():
    source = u"I:/数据/word11247relation30/file_word/file_word/"
    dest = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_1500_TFIDF/file_word/file_word_mat/"
    # reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
    # rellist=getrellist(u"I:/数据/statistic/relations.txt")
    if not os.path.exists(dest):
        os.makedirs(dest)
    refMat = getrefMat()
    rellist = getrellist()
    for file in os.listdir(source):
        # reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
        # rellist=getrellist(u"I:/数据/statistic/relations.txt")
        word = file.split(".") [0]
        print word
        getmatrixfile(source+file,word,dest+u"l_"+word,refMat,rellist)


# def test():
#     source = u"I:/数据/word11247relation30/file_word/file_word/"
#     dest = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
#     reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
#     rellist=getrellist(u"I:/数据/statistic/relations.txt")
#     getmatrixfile(source+"con.txt",dest+"con.txt".strip(".txt")  ,reflist,rellist)

# getrefMat()
# getWordMat()
# getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")


