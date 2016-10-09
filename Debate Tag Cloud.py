import string
from htmlFunctions import make_HTML_box, make_HTML_word, print_HTML_file

file = "debate.txt"
fileref = open(file, 'r')
file2 = "stopWords.txt"
fileref2 = open(file2, 'r')
obamaDict = {}
romneyDict = {}
modDict = {}
stopWords = ["mr.", "romney:", "obama:", "president", "lehrer:", "jim:", "--"]
isObama = False
isRomney = False
isMod = False
isStopWord = False
obamaList = []
romneyList = []

for line in fileref2:
    
    newline = line.lower()
    newline = line.split()

    
    

    for i in newline:
        stopWords.append(i)

for line in fileref:

    if "PRESIDENT OBAMA:" in line:
        
        isObama = True
        isRomney = False
        isMod = False

    elif "MR. ROMNEY:" in line:
        
        isRomney = True
        isObama = False
        isMod = False

    elif "JIM LEHRER:" in line:
        
        isMod = True
        isRomney = False
        isObama = False

    newLine = line.lower()
    newLine = newLine.split()

    for i in newLine:
        if i in stopWords:
            isStopWord = True

        if isStopWord == False:
            if isObama == True:
                if i in obamaDict:
                    obamaDict[i] += 1
                else:
                    obamaDict[i] = 1

            elif isRomney == True:
                if i in romneyDict:
                    romneyDict[i] += 1
                else:
                    romneyDict[i] = 1

            else:
                if i in modDict:
                    modDict[i] += 1
                else:
                    modDict[i] = 1
        isStopWord = False

for i in obamaDict:
    obamaList.append((obamaDict[i], i))
obamaList.sort()
obamaList.reverse()
print("+++++++++++++++++++++++++++++")
print("Obama : words in frequency order as count: word pairs")
for i in range(0,38,4):
    
    print(obamaList[i][0],":",obamaList[i][1], "         ", obamaList[i+1][0],":",obamaList[i+1][1], "         ", obamaList[i+2][0],":",obamaList[i+2][1], "         ", obamaList[i+3][0],":",obamaList[i+3][1])

for i in romneyDict:
    romneyList.append((romneyDict[i], i))
romneyList.sort()
romneyList.reverse()
print("+++++++++++++++++++++++++++++")
print("Romney : words in frequency order as count: word pairs")
for i in range(0,38,4):
    print(romneyList[i][0],":",romneyList[i][1], "         ", romneyList[i+1][0],":",romneyList[i+1][1], "         ", romneyList[i+2][0],":",romneyList[i+2][1], "         ", romneyList[i+3][0],":",romneyList[i+3][1])

high_count = 200
low_count = 20
body = ""
i = 0

for cnt,word in obamaList:
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    i += 1
    if i == 40:
        break
box = make_HTML_box(body)
print_HTML_file(box,'Obama')

body = ""
i = 0

for cnt,word in romneyList:
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    i += 1
    if i == 40:
        break

box = make_HTML_box(body)
print_HTML_file(box,'Romney')
