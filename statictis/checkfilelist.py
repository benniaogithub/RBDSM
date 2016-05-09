#coding:utf-8

for line in open("I:/数据/wordlist/wordlist_final3.txt"):
    line=line.strip("\n")
    for i in line:
        if i<'a' or i>"z":
            print (line)