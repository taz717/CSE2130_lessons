'''
Moataz Khallaf
files intro
Nov 19, 2018
'''
''' files and file structures
previously when only program files are used, any information stored in memory disapears
when the program is closed. using external files allows the program to store data 
persistently on the local computer or in the cloud, so that any new running of the program 
can reference the information stored on these files.

files are often text based but proprietary programs
can encrypt files so that only specifc software(programs) can open those files.

files and file structures are integral because most programs including bleeding edge ones like
neural networks, utilize file structure to process large data sets
'''

# EX1 create file
def createFile():
    fil = open("data.txt", "w")
    #w represents the mode which by default is r for read only. W = write
    return fil

openFile = createFile() 

# EX2 update file content
 
def writeFile(fil):
    fil.write("Hello world")
    return fil

# Ex2.1 closing file
def closeFile(fil):
    fil.close()

writeFile(openFile)
closeFile(openFile)

# EX 3 read file
def readFile():
    fil = open("data.txt", "r")
    return fil
openFile = readFile()
print(openFile.read())
closeFile(openFile)

# EX4 adding more info to file
def writeMore(fil, text): ##overwrites
    fil.write(text)

def append2File(): ##adds
    fil = open("data.txt", "a")
    return fil


string = "\nGoodbye World!"

openFile = append2File()
writeMore(openFile, string)
closeFile(openFile)

openFile = readFile()
print(openFile.read())

# Note: usin a file in write mode will overwrite the contents of the file and then add the info
# using a file in append mode will add the new content to the pre existing

#ex 5 reading and storing file data
openFile = readFile()
lines = openFile.read()
closeFile(openFile)
print(lines)
lines = lines.split(" ")
print(lines)

#5.1
lines[2] = "happy"
lines = " ".join(lines)
openFile = createFile()
openFile.write(lines)
openFile.close()
openFile = readFile()
print(openFile.read())

#Ex 6
import os
#os.remove("date.txt")