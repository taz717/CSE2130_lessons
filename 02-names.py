'''
moataz khallaf
saving name
Nov 19, 2018
'''

def createFile(name):
    fil = open(name, "w")
    return fil

def askName():
    name = input("shut up?")
    return name

def writeFile(fil, text):
    fil.write(text)
    fil.close()

def readFile(name):
    fil = open(name, "r")
    print(fil.read())


def appendFile(name):
    fil = open(name, "a")
    fil.write(", ")
    return fil
def menu():
    pass


fileName = input("what file?")
openFile = appendFile(fileName)
name = askName
writeFile(openFile, name)
readFile(fileName)