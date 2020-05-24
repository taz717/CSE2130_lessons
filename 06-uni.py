'''
taz
Dec 6, 2018
tuition stuffs
'''
###imports
import csv

###inpfunc
###procfunc
def calcP(a, b):
        x = (a - b) / b * 100
        return x
###outfunc
###inp
prov = input("province ")
year = input("year?(0000/0001) ")
###proc
fil = open("CanAndIntTuitFees.csv", newline = "")
readCSV = csv.reader(fil) #loads file into the csv reader which can read the table row by row

rows = []

for line in readCSV:
    rows.append(line)
#for each line the reader reads. append the line to the rows array
for i in range(len(rows)):
        if str(year) in str(rows[i][0]): #checks if the years match
                if prov in rows[i][1]: #checks if the prov matches
                        if "Canadian undergraduate" in rows[i][3]: #checks if it's for undergrad
                                currentYear = rows[i] #ty for the info

currentYear[0] = currentYear[0].split("/") #splits the years to help get the year before 

for i in range(len(rows)):
        if currentYear[0][0] in rows[i][0]: #narrows down the search for dates
                pastYear = rows[i] #picks every date in that area then narrows down the info by...
                pastYear[0] = pastYear[0].split("/") #spliting the date to get the second number and
                if pastYear[0][1] == currentYear[0][0]: #making sure it matches the first num in the current year
                        if prov in rows[i][1]: #ensures it's the right prov
                                if "Canadian undergraduate" in rows[i][3]: #ensures it's undergrad
                                        break
        else:
                pass

tut1 = currentYear[10]
tut2 = pastYear[10]
Pchange = calcP(int(tut1), int(tut2))
###out
print("the percent change between this year and last is", Pchange,)
'''
so if the comments don't help. essentially the second for i in range statement picks every piece of data
and makes sure that it's matching the current year for everything except that the 1st year of the school
year is the second in the second past year var to make sure that you are actually taking info from the
year before. if all the if statements match then it just takes that var and breaks the entire thing
if one if statement doesn't match then it just passes the entire thing.
'''