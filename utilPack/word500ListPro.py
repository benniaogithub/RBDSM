#!/usr/bin/env python
# encoding: utf-8

"""
@author: yx@xy
@license: Apache Licence 
@file: word500ListPro.py
@time: 2016/5/8 0:24
"""

def preProcess():
    wfile = open("../res/500WordListNEW.txt","w")
    for line in open("../res/500WordList.txt"):
            word = line.strip().split(":")[0].split(" ")[0].lower()
            # print(word)
            line2 = word
            synonymsExist = line.strip().find("Synonym:")
            synonyms = None
            if(synonymsExist>-1):
                synonyms = line.strip().split("Synonym:")[1]
                # print(synonyms)
            else:
                synonymsExist = line.strip().find("Synonyms:")
                if(synonymsExist>-1):
                    synonyms = line.strip().split("Synonyms:")[1]
                    # print(synonyms)
            if  synonyms :
                # print(synonyms.split(".")[0])
                line2 = line2+"\t" + "Synonyms:"
                synonyms = synonyms.split(".")[0].split(",")
                for synonym in synonyms:
                    synonym = synonym.strip().split(":")[0].split(";")[0].split(" (")[0]
                    if(len(synonym.split(") "))>1):
                        synonym = synonym.split(") ")[1]
                    line2 = line2+synonym+","
                    # print(synonym)
                line2 = line2+"\t"
            # print(line.strip())
            # print(line2)
                #print(synonyms)


            antonymsExist = line.strip().find("Antonym:")
            antonyms = None
            if(antonymsExist>-1):
                antonyms = line.strip().split("Antonym:")[1]

            else:
                antonymsExist = line.strip().find("Antonyms:")
                if(antonymsExist>-1):
                    antonyms = line.strip().split("Antonyms:")[1]


            if  antonyms :
                # print(antonyms.strip())
                line2 = line2 +"\t"+ "Antonyms:"
                antonyms = antonyms.split(",")
                for antonym in antonyms:

                    antonym = antonym.strip().split(":")[0].split(";")[0].split(" (")[0].split(".")[0]
                    # antonym = antonym.strip()
                    # print(antonym)
                    if(len(antonym.split(") "))>1):
                        antonym = antonym.split(") ")[1]
                    line2 = line2+antonym+","
                    # print(antonym)


            # print(line2)
            # print(line.strip())
            if(len(line2.split("\t"))>1):
                wfile.write(line2+"\n")
    wfile.close()

def getWordList():
    rfile = open("../res/vocab.txt")
    wordList = []
    for line in rfile:
        wordList.append(line.strip("\n"))
    rfile.close()
    # arr = np.array(wordList)
    return  wordList

def findNotExistWord():

    wordlist = getWordList()
    wordNotExist = []
    for line in open("../res/500WordListNEW.txt"):
        word = line.split("\t")[0]
        if  not word in wordlist:
            wordNotExist.append(word)

        synonymsExist = line.strip().find("Synonyms:")
        synonyms = None
        if(synonymsExist>-1):
            synonyms = line.strip().split("Synonyms:")[1]
            synonyms = synonyms.split(",")
            for synonym in synonyms:
                synonym = synonym.split("Antonyms:")[0].strip()
                if synonym:
                    if not synonym in wordlist:
                        wordNotExist.append(synonym)


        antonymsExist = line.strip().find("Antonyms:")
        antonyms = None
        if(antonymsExist>-1):
            antonyms = line.strip().split("Antonyms:")[1]
            antonyms = antonyms.split(",")
            for antonym in antonyms:
                if antonym:
                    # print(antonym)
                    if not antonym in wordlist:
                        wordNotExist.append(antonym)

    wfile = open("../res/wordNotExist.txt","w")
    wfile.writelines(item+'\n' for item in wordNotExist)