'''
Moataz Khallaf
avg calc 
Nov 28, 2018
'''
import sys, random
yes = True

###inputsFunc
def menu():
    x = input(''' Hello welcome to the autamated grading agent in networking also known as AGAIN.
    please pick an option
    1) enter a class with grade
    2) edit a grade for a class
    3) wipe all history
    4) exit
    
    ''')
    return x

def askInformation():
    x = input("Please enter your grade followed by the subect")
    return x

def moreClass():
    x = input("would you like to enter anouther class Y/N")
    return x

###procFunc

def createFile(name):
    try:
        fil = open(name, "w")
        return fil
    except FileExistsError:
        pass

###outputsFunc

### Code start ###

###inputs
oof = menu()
fil = input('''please create the name of your avg file.
(name) (grade) (year)
''')

list1D = askInformation()
list1D = list1D.split(" ")
print(list1D)
list2D = []
list2D.append(list1D)




while yes:
    x = moreClass()
    x = x.lower()
    if x == "n":
        yes = False
        break
    else:
        list1D = askInformation()
        list1D = list1D.split(" ")
        list2D.append(list1D)   


###proc
createFile(fil)
while True:
    avgList = 0
    for i in range(len(list2D)):
        list2D[i][0] = int(list2D[i][0])
        try:
            avgList = (avgList + list2D[i][0])
        except ZeroDivisionError:
            pass
    avgList = avgList / len(list2D)
    break
avgList = str(avgList)
fil = open("test", "w")
fil.write(avgList)
fil.close
for i in range(len(list2D)):
        list2D[i][0] = str(list2D[i][0])
        list2D[i] = " ".join(list2D[i])
list2D = ", ".join(list2D)
fil = open("test", "a")
fil.write(list2D)
fil.close