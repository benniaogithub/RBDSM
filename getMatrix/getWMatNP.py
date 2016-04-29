# encoding: utf-8
import os
import numpy as np

def getreflist(filename):
    count=0
    reflist = []
    for line in open(filename):
        if count==5000:break
        reflist.append(line.split("----")[0])
        count+=1
    arr = np.array(reflist)
    np.save("../res/reflist.npy",arr)
    return reflist

def getrellist(filename):
    rellist=[]
    for line in open(filename):
        rellist.append(line.strip("\n"))
    arr = np.array(rellist)
    np.save("../res/rellist.npy",arr)   #npy可不加
    return rellist

def getmatrixfile(sourcefile,destfile,reflist,rellist):
    result = np.zeros( (len(reflist),len(rellist)))
    for line in open(sourcefile):
        linelist=line.strip("\n").split("\t")
        if linelist[0] in reflist and linelist[1] in rellist:
            result[reflist.index(linelist[0]),rellist.index(linelist[1])]=int(linelist[2])
    # wfile=open(destfile,"w")
    np.save(destfile,result)
#
def main():
    source = u"I:/数据/word11247relation30/file_word/file_word/"
    dest = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
    for file in os.listdir(source):
        reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
        rellist=getrellist(u"I:/数据/statistic/relations.txt")
        print file
        getmatrixfile(source+file,dest+file,reflist,rellist)


# def test():
#     source = u"I:/数据/word11247relation30/file_word/file_word/"
#     dest = u"I:/数据/word11247relation30/file_word/file_word_matrix_npy/"
#     reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
#     rellist=getrellist(u"I:/数据/statistic/relations.txt")
#     getmatrixfile(source+"con.txt",dest+"con.txt".strip(".txt")  ,reflist,rellist)

# test()
if __name__ == '__main__':
    main()
# getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")


