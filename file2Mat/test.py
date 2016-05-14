#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: test.py
@time: 2016/4/19 19:17
"""
import numpy as np
from scipy import stats


def getRelList():
    rellist=[]
    for line in open("../res/relations.txt"):
        rellist.append(line.strip("\n"))
    # arr = np.array(rellist)
    # sio.savemat("rellist.mat",{"rellist":arr},oned_as='row')
    # np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist
def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)

    return  wordList

np.set_printoptions(threshold='nan')
# root = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
# arr = np.load(root+"zoo.txt.npy")
# print arr
# # refArr = np.load("res/reflist.npy")
# # relArr = np.load("res/rellist.npy")
# # print relArr
# # print refArr


# root = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
# w1Mat = np.load(root+"a.txt.npy")
# w2Mat = np.load(root+"able.txt.npy")
# for i in range(0,np.shape(w1Mat)[1]):
#     print w1Mat[:,i]

# print stats.spearmanr([6,12,123,432,65], [1,2,3,4,5])
#
# root = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
# w1Mat = np.load(root+"a.txt.npy")
# w2Mat = np.load(root+"a.txt.npy")
# sim = 0
# for i in range(0,np.shape(w1Mat)[1]):
#     v1 = w1Mat[:,i]
#     v2 = w2Mat[:,i]
#
#     break

# def vecSim(x, y):
#     result1 = 0.0
#     result2 = 0.0
#     result3 = 0.0
#     for i in range(len(x)):
#         result1 += x[i] * y[i]  # sum(X*Y)
#         result2 += x[i] ** 2  # sum(X*X)
#         result3 += y[i] ** 2  # sum(Y*Y)
#     try:
#         print result1
#         print np.dot(x,y)
#         print result1 / ((result2 * result3) ** 0.5)
#
#     except ZeroDivisionError:
#         return 1.0
# vecSim([1,-1,0],[2,-1,3])

# def vecSim(x,y):
#     print x
#     print y
#     result1 = np.dot(x,y)
#     result2 = np.linalg.norm(x)
#     result3 = np.linalg.norm(y)
#     print result1
#     print result2
#     print result3
#     if(result2*result3 == 0):
#         return 1
#     print result1/(result2*result3)
#
# vecSim([1.0,0.01],[1.0,32])

# def getWordList():
#     rfile = open("../res/vocab.txt")
#     wordList = []
#     for line in rfile:
#         wordList.append(line.strip("\n"))
#     rfile.close()
#     return  wordList
#
# WSList = []
# wordList = getWordList()
#
# for line in open("../res/WS-353.txt"):
#         w1 = line.split("\t")[0].lower()
#         w2 = line.split("\t")[1].lower()
#         if w1 not in wordList:
#             WSList.append(w1)
#         if w2 not in wordList:
#             WSList.append(w2)
#
# print WSList
'''
from scipy import linalg
a = np.random.randn(5000, 3000)

U, s, Vh = linalg.svd(a)
print U.shape, Vh.shape, s.shape
'''
# import numpy as np
# from scipy import linalg
#
# rel = np.floor(np.random.randn(12000, 5000))
# U, s, Vh = linalg.svd(rel)
#
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from numpy.linalg import solve, norm
from numpy.random import rand
from scipy.sparse.linalg import svds
from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
from scipy.sparse import vstack
import scipy.io as sio
import time
import os

# A = lil_matrix((10, 5))
# A[0, :15] = rand(100)
# A[1, 5:10] = A[0, :5]
# A.setdiag(rand(10))
# print A.shape
# [u,s,v] = svds(A,ncv=None, tol=0, which='LM', v0=None, maxiter=None, return_singular_vectors="u")
# print u.shape
# print s
#
# A = csr_matrix([[1.0, 2, 0], [0, 0, 3], [4, 0, 5]])
# print A.toarray()
# [u,s,v] = svds(A,k=1,return_singular_vectors="u")
# sio.savemat("A.mat",{"Ab":A},oned_as='row')
#
# print sio.whosmat("A.mat")
# nRow,nCol=A.get_shape()
# print type(A)
# print A[:,2]
# print u

# def generateTestMat(size):
#         '''''generate a test matrix for k-eigenvalues problem
#         '  matlab and scipy.sparse.linalg.eigs seem use the same package ARPACK
#         '  this matrix has two diagnol lines, one is on the diagnol and the other is off 1
#         '''
#         # A = lil_matrix((size, size))
#         # A[0,:size]=np.random.rand(size)
#         # A.setdiag(np.random.rand(size))
#         # A.setdiag(np.random.rand(size-1),1)
#         #保存成matlab可以读取的格式，{"A":A}前面的A表示在matlab中的名字，后面的A表示在python中名字
#         A = csr_matrix([[1.0, 2, 0], [0, 0, 3], [4, 0, 5]])
#         sio.savemat("A.mat",{"A":A},oned_as='row')
#         print("generate a test matrix,with size %s by %s" %(size,size))
#
# def calculateSVDs(tolerance=0):
#
#         A=sio.loadmat("A.mat")["A"]#后面的A表示在matlab中名字
#         timeCheckin=time.clock()
#         #tol=0表示使用原先的计算精度
#         [u,s,v] = svds(A,k=1,return_singular_vectors="u",tol=tolerance)
#
#         print u.shape
#         print u
#         print(" cost %s seconds" % (time.clock()-timeCheckin))
#
# generateTestMat(10000)
# calculateSVDs(tolerance=0.001)

# B = csc_matrix([[1.0, 2, 0], [0, 0, 3], [4, 0, 5]])
# A = csc_matrix([1.0, 2, 0],)
#
# relMat = vstack([A,B],format="csc")
# print relMat.get_shape()
# dest = u"I:/数据/word11247relation30/file_word/file_word_matrix_mat/abbot.txt.mat"
# print  sio.whosmat(dest)
# B = csc_matrix([[1.0, 2, 0], [0, 0, 3]]).transpose()
# sio.savemat("test.mat",{"test":B},oned_as='column')
# print "tet"+str(1)
# print B.get_shape()

# b = np.ones((1,3), dtype = int)
# b[0,:] = [2,3,4.5]
# a = np.vstack([b,b])
#
# print b
# print a[0,1:]

# def getRelList():
#     relList = sio.loadmat("../res/rellist.mat")["rellist"].tolist()
#     return  relList
#
# def getWordList():
#     wordlist = sio.loadmat("../res/wordlist.mat")["wordlist"].tolist()
#     print wordlist
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
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)

    return  wordList


# def yzrmtwm():                 #验证tmtwm 是否正确
    # relpath = u"I:/数据/word11247relation30/rel_matrix/rel_mat_latent_100/r_acl.mat"
    # # relspath = u"I:/数据/word11247relation30/rel_matrix_s/rel_mat_latent_100/r_acl.mat"
    # wordpath = u"I:/数据/word11247relation30/file_word/word_mat_latent_100/"
    # # print getRelList()
    # # getWordList()
    # wordlist = getWordList()
    # reltestmat = sio.loadmat(relpath)["acl"]
    # # for i in range(0,len(wordlist)):
    # #     word = wordlist[0]
    # #     wordmat = sio.loadmat(wordpath+"l_"+word+".mat")[word]
    # #     print np.linalg.norm(wordmat[0,:]-reltestmat[i,:])
    # word = wordlist[0]
    # wordmat = sio.loadmat(wordpath+"l_"+word+".mat")[word]
    # print reltestmat[0,:]
    # print wordmat[0,:]-reltestmat[0,:]
    # print np.linalg.norm(wordmat[0,:]-reltestmat[0,:])


#
def uMults(dim):            #  将矩阵和s相乘
    relpath = u"I:/数据/word11247relation30/rel_matrix_ls/rel_mat_latent_"
    relpath = relpath+str(dim)+u"/"
    relspath = u"I:/数据/word11247relation30/rel_matrix_s/rel_mat_latent_"
    relspath = relspath+str(dim)+u"/"
    # dest = u"I:/数据/word11247relation30/file_word_lus/rel_mat_latent_"
    dest = u"I:/数据/word11247relation30/test/rel_mat_latent_"
    dest = dest+str(dim)+u"/"
    rellist = getRelList()
    if not os.path.exists(dest):
                os.makedirs(dest)
    for i in range(0,len(rellist)):
            rel = rellist[i]
            relmat = sio.loadmat(relpath+"r_"+rel+".mat")[rel]
            relsmat = sio.loadmat(relspath+"r_"+rel+".mat")[rel].T
            # print relsmat.shape
            # relsmat = np.diag(relsmat)
            # print relsmat
            relusmat = relmat*relsmat
            print relusmat.shape

            sio.savemat(dest+"r_"+rel+".mat",{rel:relusmat},oned_as='column')


# A = np.array( [[1,1],[0,1]] )
# C = np.diag([2,1])
# print C
# B = np.array( [[2,0],[0,4]] )
# print A.dot(B)

# A = np.array( [[1,5],[0,1]] )
# C = np.array([3,2])
# print A*C
# B = np.array( [[2,0],[0,4]] )
# print A.dot(B)

# uMults(350)

# from sklearn import datasets
# iris = datasets.load_iris()
# print np.unique(iris.target)
# # print iris.data.shape
# print iris.target.shape

# digits = datasets.load_digits()
# digits.images.shape
# import pylab as pl
# pl.imshow(digits.images[0], cmap=pl.cm.gray_r)
# pl.show()

# from sklearn import svm
# clf = svm.LinearSVC()
# clf.fit(iris.data, iris.target) # learn from the data
# print clf.predict([[ 5.0,  3.6,  1.3,  0.25]])
#
# print clf.coef_

# from scipy import misc
# from sklearn import cluster

# lena = misc.lena().astype(np.float32)
# X = lena.reshape((-1, 1)) # We need an (n_sample, n_feature) array\
# k_means = cluster.KMeans(5)
# values = k_means.cluster_centers_().squeeze()
# print values.shape
# labels = k_means.labels_
# lena_compressed = np.choose(labels, values)
# lena_compressed.shape = lena.shape
# k_means.fit(X)

# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer()
# corpus = ['This is the first document.','This is the second second document.','And the third one.','Is this the first document?',]
# X = vectorizer.fit_transform(corpus)
# print X.toarray()
# print vectorizer.get_feature_names()


#TFIDF

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# transformer = TfidfTransformer()
# counts = [[3, 0, 1],[2, 0, 0],[3, 0, 0], [4, 0, 0],[3, 2, 0],[3, 0, 2]]
# tfidf = transformer.fit_transform(counts)
# print tfidf.toarray()

# from sklearn.feature_extraction.text import TfidfTransformer
# relpath = u"I:/数据/word11247relation30/rel_matrix/rel_mat/"
# dest = u"I:/数据/word11247relation30/rel_matrix/rel_mat_TFIDF/"
# if not os.path.exists(dest):
#             os.makedirs(dest)
# rellist = getRelList()
# transformer = TfidfTransformer()
#
# for i in range(0,len(rellist)):
#             rel = rellist[i]
#             relmat = sio.loadmat(relpath+"r_"+rel+".mat")[rel]
#             tfidf = transformer.fit_transform(relmat)
#             relTFIDF = tfidf.toarray()
#             print relTFIDF.shape
#             sio.savemat(dest+"r_"+rel,{rel:relTFIDF},oned_as='column')

# import theano
# theano.test()

# b = np.array(['abb','b','c'])
# print 'b' in b
# # a = np.argsort(b)
# # print a
# print np.where(b=='b')[0][0]
# print b[a][-3:]

# root = u"I:/数据/word11247relation30/rel_30_ref_5000/rel_svd/file_word_lus/word_matus_latent_300/"
root = u"I:/数据/word11247relation30/rel_30_diffref_TFIDF/ref_1500_TFIDF/file_word/file_word_mat/"
w1Mat = sio.loadmat(root+u"l_a.mat")["a"].todense()
print(w1Mat[:,6])