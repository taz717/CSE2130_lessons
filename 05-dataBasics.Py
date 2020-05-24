'''
Moataz Khallaf
data base basics
Dec 4, 2018
'''

''' data bases. what and why
a data base is a collections of information that is organized so that it can be
easily accessed, managed and updated

data is organized into rows and columns of tables and is indexed to make it easier to find
relevent information.

data gets updated, expanded and deleted as new information is added.
the data within a database is called a dataset and because of their size, often times only
a few lines are printed at a time

so to give u an idea of the magnitude of size we are talking about. currently our csv has 700ish lines
and 10 columns ... about 71 000 bytes.

max before splitting into multiple files is 140 terabytes... 1400000000000000 bytes
but that makes it insanly small. so most people stick to abuot 40 000lines

there are many types of databases. commonly 2d tables, relational and key-pair are common 
database formates
comma seperated value tables (csv) are a commonly used 2d table
'''

import csv
### reading and searching csv files

fil = open("comicBookCharData.csv", newline = "")
readCSV = csv.reader(fil) #loads file into the csv reader which can read the table row by row

rows = []

for line in readCSV:
    rows.append(line)
#for each line the reader reads. append the line to the rows array

### view the data
'''
limit = 0
for i in range(len(rows)):
    if limit <= 10 and rows[i][-1] == "Marvel":
        print(" | ".join(rows[i]))
        limit += 1
    else:
        break #end loop and move to next instructions
'''
#limit var builds in a natural stopping point for printing the data; however, the program will still run
#through the rest of the rows in the table. Therefore the program should also stop the for loop when the
#search is complete

'''
databases are only has effective the program is to search for a specific data.
therefore adjust the print code above to display the following information.

    1.bottom ten values
    2.top ten good chars
    3.top five chars with secret identities
    4.top ten chars first introduced in 2003
'''
'''
limit = 0
for i in range(len(rows)):
    limit += 1
    if limit <= 699:
        pass
    else:
        print(" | ".join(rows[i]))
        #end loop and move to next instructions
'''
'''
limit = 0
for i in range(len(rows)):
    if limit <= 10:
        print(" | ".join(rows[-i]))
        limit += 1
    else:
        break #end loop and move to next instructions
'''
'''
limit = 0
for i in range(len(rows)):
    if limit <= 10 and "Good Characters" in rows[i][2]:
        print(" | ".join(rows[i]))
        limit += 1
    else:
        pass #end loop and move to next instructions
    if limit == 11:
        break
'''
''''
limit = 0
for i in range(len(rows)):
    if limit <= 10 and rows[i][-1] == "Marvel":
        print(" | ".join(rows[i]))
        limit += 1
    else:
        break #end loop and move to next instructions
'''
### appending + updating values
# in order to append a new value, since the database is in a 2d array, the new values append
# onto the array

rows.append([
    'taz manian', 'Syntaz', 'Bad Characters', 'Earth-616', 'Brown Eyes', 'Black Hair', 'Living Characters',
     '1', 'O7-OCT', '2018', 'Marvel'])

## update
'''
when updating multiple values within a database. a for loop is used to identify
the rows that need updating

once the updating is complete and saved. there is no way to revert to the previous data without a 
back up of the data base

much of database design relies on how the will be used than what data is being collected
'''
limit = 0
for i in range(len(rows)):
    if limit <= 10:
        if "New Earth" in rows[i][0]:
            rows[i][0] = rows[i][0].split(" (")
            rows[i][0].pop()
            rows[i][0] = " (".join(rows[i][0])

            #print(" | ".join(rows[i]))
            #limit += 1
    else:
        pass #end loop and move to next instructions
    if limit == 11:
        break
for i in range(len(rows)):
    if limit <= 10:
        if "Earth-616" in rows[i][0]:
            rows[i][0] = rows[i][0].split(" (")
            rows[i][0].pop()
            rows[i][0] = " (".join(rows[i][0])

            #print(" | ".join(rows[i]))
            #limit += 1
    else:
        pass #end loop and move to next instructions
    if limit == 11:
        break
for i in range(len(rows)):
    if limit <= 10:
        if "Eyes" in rows[i][3]:
            rows[i][3] = rows[i][3].split(" ")
            rows[i][3].pop()
            rows[i][3] = " ".join(rows[i][3])

            #print(" | ".join(rows[i]))
            #limit += 1
    else:
        pass #end loop and move to next instructions
    if limit == 11:
        break
for i in range(len(rows)):
    if limit <= 10:
        if "Hair" in rows[i][4]:
            rows[i][4] = rows[i][4].split(" ")
            rows[i][4].pop()
            rows[i][4] = " ".join(rows[i][4])

            #print(" | ".join(rows[i]))
            #limit += 1
    else:
        pass #end loop and move to next instructions
    if limit == 11:
        break
### write to database file
fil = open("UP_comicBookCharData.csv", "w", newline="")
wrtieCSV = csv.writer(fil)

for i in range(len(rows)):
    wrtieCSV.writerow(rows[i])
    #fo shizzel my nizzel
    #for each line in the rows array, the csv writer will write a row in the database and close
