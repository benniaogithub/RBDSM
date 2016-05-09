#coding:utf-8
import os
import scipy.io as sio

result={}
reflist=[]
rellist=[]


for line in open("../res/relations.txt"):
    rellist.append(line.strip("\n").strip())
    result.setdefault(line.strip("\n").strip(),{})
for file in os.listdir(u"I:/数据/word12585relation30/file_word/"):
    print file
    for line in open(u"I:/数据/word12585relation30/file_word/"+file):
        linelist=line.strip("\n").split("\t")
        rel=linelist[1]
        ref=linelist[0]
        if ref not in reflist:
            reflist.append(ref)
        count=int(linelist[2])
        if not result[rel].has_key(ref):
            result[rel].setdefault(ref,count)
        else:
            result[rel][ref]+=count

wfile=open("ref.txt","w")
for item in reflist:
    wfile.write(item+"\n")
wfile.close()

newresult=[[0 for col in range(len(reflist))] for row in range(30)]
for i in range(len(rellist)):
    for j in range(len(reflist)):
        if result[rellist[i]].has_key(reflist[j]):
            newresult[i][j]=result[rellist[i]][reflist[j]]
        else:
            pass

sio.savemat(u"I:/数据/word12585relation30/result.mat",{"result":newresult})

