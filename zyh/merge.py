#coding:utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: merge.py
@time: 2016/5/8 11:20
"""
import os
import re

def merge(source,dest):
    for file in os.listdir(source):
        print file
        sdic={}
        for line in open(source+file):
            linelist=line.strip("\n").split("\t")
            if sdic.has_key(linelist[0]):
                sdic[linelist[0]]+=1
            else:
                sdic.setdefault(linelist[0],1)
        rlist=sorted(sdic.items(), key=lambda sdic:sdic[0])
        wfile=open(dest+file,"w")
        '''
        for item in sdic:
            wfile.write(item+"\t"+str(sdic[item])+"\n")
            '''
        for item in rlist:
            wfile.write(item[0]+"\t"+str(item[1])+"\n")
        wfile.close()

def file100(source,dest):
    wfile=open(dest+"0.txt","w")
    count=0
    filecount=0
    print os.listdir(source)
    for sefile in os.listdir(source):
        print sefile
        for file in os.listdir(source+sefile+"/"):
            print file
            for line in open(source+sefile+"/"+file):
                if count==5500000:
                    count=0
                    filecount+=1
                    wfile.close()
                    wfile=open(dest+str(filecount)+".txt","w")
                wfile.write(line)
                count+=1
    wfile.close()



def filebyalpha(source,dest):
    for i in range(97,123):
        wfile=open(dest+str(chr(i))+".txt","w")
        wfile.close()
    allist=[]
    alp='a'
    for file in os.listdir(source):
        for line in open(source+file):
            if line[0]==alp:
                allist.append(line)
            else:
                wfile=open(dest+alp+".txt","a")
                for l in allist:
                    wfile.write(l)
                allist=[]
                wfile.close()
                if alp=='z':
                    alp='a'
                else:
                    alp=str(chr(ord(alp[0])+1))
def remove1(source,dest):
    lines=0
    for file in os.listdir(source):
        print file
        wfile=open(dest+file,"w")
        for line in open(source+file):
            linelist=line.strip("\n").split("\t")
            if int(linelist[1])==1:
                continue
            else:
                wfile.write(line)
                lines+=1
        wfile.close()
    print lines

def fileword(source,dest):
    word=""
    wordlines=[]
    for file in os.listdir(source):
        print file
        for line in open(source+file):
            linelist=re.split("----|\t",line.strip("\n"))
            print len(linelist)
            cword=linelist[0]
            if word!=cword:
                if word!="":
                    wfile=open(dest+word+".txt","w")
                    for l in wordlines:
                        wfile.write(l)
                    wfile.close()
                    wordlines=[]
                wordlines.append("\t".join(linelist[1:])+"\n")
                word=cword
            else:
                wordlines.append("\t".join(linelist[1:])+"\n")

#file100(u"I:\\数据\\corpus\\extractedAdd\\","temp1\\")
#merge("temp1\\","temp2\\")
#remove1("temp2\\","temp3\\")
fileword("temp3\\","temp4\\")