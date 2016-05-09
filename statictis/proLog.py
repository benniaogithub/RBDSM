file = open("4.4.txt")
fileout = open("logDebug2.txt","w")

b = False
for line in file:
    if b == True:
        fileout.write(line)
        b = False
    elif line.startswith("[DEBUG]"):
        b = True
        fileout.write(line)

fileout.close()
file.close()