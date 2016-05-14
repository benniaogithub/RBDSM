# encoding: utf-8
import os
import sys
#每个单词一个文件
def getreflist(filename):
    count=0
    reflist=[]
    for line in open(filename):
        if count==5000:break
        reflist.append(line.split("----")[0])
        count+=1
    return reflist
def getrellist(filename):
    rellist=[]
    for line in open(filename):
        rellist.append(line.strip("\n"))
    return rellist
def getmatrixfile(sourcefile,destfile,reflist,rellist):
    result=[]
    for i in range(len(reflist)):
        temp=[0 for i in range(len(rellist))]
        result.append(temp)
    for line in open(sourcefile):
        linelist=line.strip("\n").split("\t")
        if linelist[0] in reflist and linelist[1] in rellist:
            result[reflist.index(linelist[0])][rellist.index(linelist[1])]=int(linelist[2])
    wfile=open(destfile,"w")
    for i in range(len(result)):
        newline=""
        for j in range(len(result[i])):
            newline+=str(result[i][j])+" "
        wfile.write(newline.strip()+"\n")
    wfile.close()
def main():
    source="I:/file_word/file_word/"
    dest="I:/file_word/file_word_ matrix/"
    for file in os.listdir(source):
        reflist=getreflist(u"I:/数据/statistic/referenceCount-112189530.txt")
        rellist=getrellist(u"I:/数据/statistic/relations.txt")
        getmatrixfile(source+file,dest+file,reflist,rellist)

if __name__ == '__main__':
    main()


