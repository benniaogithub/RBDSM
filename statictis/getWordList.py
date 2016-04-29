import os

wordlist={}
wfile=open("vocab.txt","w")
for file in os.listdir("file_word/"):
	wordlist[file[0:-4]]=1
	wfile.write(file[0:-4]+"\n")
print len(wordlist)
wfile.close()
	