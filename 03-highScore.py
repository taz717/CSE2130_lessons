'''
MoatazKhallaf
Nov 22, 2018
highScore.poi
'''
def liSort1(li):
    li.sort(key = lambda x:x[1])
    return li

fil = open("03_score.txt", "r")
text = fil.read()
fil.close()

text = text.split(', ')
for i in range(len(text)):
    text[i] = text[i].split(" ")
    text[i][0] = int(text[i][0])
print(text)

x = str(int(input("what is ur score? (000)")))
y = input("what is your name? (AAA)")
score = []

score.append(int(x))
score.append(y)


for i in range(len(text[i])+1):
    if int(score[0]) > int(text[i][0]):
        text.pop(i)
        text.append(score)

for i in range(len(text)):
        text[i][0] = str(text[i][0])
        text[i] = " ".join(text[i])
liSort1(text)
text = ", ".join(text)
fil = open("03_score.txt", "w")
fil.write(text)
fil.close