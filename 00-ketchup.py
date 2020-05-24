'''
files are stored in vars
fil = open("filename.txt", "mode") #mode = x, r, w or a
 x --> check if it exists
    functions to write default info if file is new
 r -->read
    to access date of any kind
w --> write/ overwrite
    erases current data to add new data
a --> append
    adds new content to the end of existing content


closing files:
    fil.close() removes file from memory (RAM)

    it defaults to read by the way


text = boing.read()
close.boing
and text
text = "".join(text)
fil = open("text.txt", "w")
fil.write(text)
fil.close