#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: svds.py
@time: 2016/4/25 5:14
"""
from scipy.sparse.linalg import svds
import scipy.io as sio
import time
import os
from matTrans import rmTowm12585 as rmTowm
# from scipy.sparse import hstack
# import numpy as np

# def getRelList():
#     relList = sio.loadmat("../res/rellist.mat")["rellist"].tolist()
#     return  relList

# def getWordList():
#     wordlist = sio.loadmat("../res/wordlist.mat")["wordlist"].tolist()
#
#     return  wordlist

def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    # arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist

def getWordList():
    rfile = open("../res/vocab12585.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def calculateSVDs(tolerance=0.0001,dim = 400):
        # source = u"I:/数据/word11247relation30/rel_matrix/rel_mat_TFIDF/"
        # dest = u"I:/数据/word11247relation30/rel_svd_TFIDF/rel_matrix_ls/rel_mat_latent_"
        # dests = u"I:/数据/word11247relation30/rel_svd_TFIDF/rel_matrix_s/rel_mat_latent_"
        # destus = u"I:/数据/word11247relation30/rel_svd_TFIDF/rel_matrix_lus/rel_mat_latent_"

        source = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_matrix/rel_mat/"
        # dest = u"I:/数据/word12585relation30/rel_30_ref_5000/rel_svd/rel_matrix_ls/rel_mat_latent_"
        # dests = u"I:/数据/word11247relation30/rel_30_ref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/rel_matrix_s/rel_mat_latent_"
        destus = u"I:/数据/word12585relation30/rel_30_ref_TFIDF/ref_800_TFIDF/rel_svd/rel_matrix_lus/rel_mat_latent_"

        # source = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_matrix/rel_mat/"
        # dest = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/rel_matrix_ls/rel_mat_latent_"
        # dests = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/rel_matrix_s/rel_mat_latent_"
        # destus = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_"+str(refdim)+u"_TFIDF/rel_svd/rel_matrix_lus/rel_mat_latent_"

        # dest = dest+str(dim)+u"/"
        # dests = dests+str(dim)+u"/"
        destus = destus+str(dim)+u"/"
        # if not os.path.exists(dest):
        #     os.makedirs(dest)
        # if not os.path.exists(dests):
        #     os.makedirs(dests)
        rellist = getRelList()
        if not os.path.exists(destus):
            os.makedirs(destus)
        for i in range(0,len(rellist)):
            relName = rellist[i]
            relmat = sio.loadmat(source+"r_"+relName+".mat")[relName]

        # for file in os.listdir(source):
        #     print file
        #     relName = file.split(".")[0].split("_")[1]
        #     relmat = sio.loadmat(source+file)[relName]#后面的A表示在matlab中名字
            timeCheckin=time.clock()
            #tol=0表示使用原先的计算精度
            [u,s,v] = svds(relmat,k=dim,return_singular_vectors="u",tol=tolerance)
            s = s.T
            relusmat = u*s
            # print relsmat
            # print relsmat.shape
            # relusmat = relmat.dot(relsmat)
            sio.savemat(destus+"r_"+relName+".mat",{relName:relusmat},oned_as='column')
            # sio.savemat(dest+"r_"+relName+".mat",{relName:u},oned_as='column')
            # sio.savemat(dests+"r_"+relName+".mat",{relName:s},oned_as='column')
            print u.shape
            print(" cost %s seconds" % (time.clock()-timeCheckin))

def SVDs():
    calculateSVDs(tolerance=0.001,dim = 324 )
    # calculateSVDs(tolerance=0.001,dim = 3240)
    # calculateSVDs(tolerance=0.001,refdim=refdim,dim = 400)
    # calculateSVDs(tolerance=0.001,refdim=refdim,dim = 500)
    # calculateSVDs(tolerance=0.001,dim = 800)
    # calculateSVDs(tolerance=0.001,dim = 1000)
    # calculateSVDs(tolerance=0.001,dim = 1200)
    # calculateSVDs(tolerance=0.001,dim = 1500)
    rmTowm.rmTowmByGrouplus(dim = 324)
    # rmTowm.rmTowmByGrouplus(dim = 350)


SVDs()
# calculateSVDs(tolerance=0.001,dim = 350)
# calculateSVDs(tolerance=0.001,dim = 300)
# calculateSVDs(tolerance=0.001,dim = 400)



# SVDs(refdim=1000)
# SVDs(refdim=1500)
# SVDs300(refdim=300)
# generateTestMat(10000)
# calculateSVDs(tolerance=0.001)
# generateRelMat()

