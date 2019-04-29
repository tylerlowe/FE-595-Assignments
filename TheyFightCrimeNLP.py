import glob
from textblob import TextBlob
import numpy as np


def mergeAllDataFiles():
    male = [] 
    female = []
    maleLines = []
    femaleLines = []
    for filename in glob.glob('C:\\github\\python\\datafiles/*.txt'):
        if 'female' in filename.lower() or 'she' in filename.lower() or    'women' in filename.lower() or 'femalecharacter' in filename.lower() or 'woman' in filename.lower() or 'Female-2' in filename.lower():
            female.append(filename)
        else:
            male.append(filename)

   
    for i in range (len(male)):
        with open(male[i]) as file: 
            lines=[(line) for line in (file)]
            if len(lines) == 1:              
                pass
            else:
                maleLines.extend(lines)
           
       
    for i in range (len(female)):
        with open(female[i]) as file: 
            lines=[(line) for line in (file)]
            if len(lines) == 1:               
                pass
            else:
                femaleLines.extend(lines)


    TotalLines = maleLines + femaleLines
    return TotalLines, maleLines, femaleLines

def sentimentalayisis(Lines, LinesF):
    male = []
    female = []
    for item in Lines:
        male.append(TextBlob(item).sentiment[0])
        
    for item in LinesF:
        female.append(TextBlob(item).sentiment[0])
    Best = Lines[np.argmax(male)] + LinesF[np.argmax(female)]
    Worst = Lines[np.argmin(male)] + LinesF[np.argmin(female)] + 'They fight crime!'
    return Best, Worst


def topdescriptions(Final):
    adj = []
    for i in range(len(Final)):
        adj.extend(Final[i].strip(' ').split(' ')[2:4])
    ADJ = ' '.join(adj)

    common = {}
    for item in ADJ.split(' '):
        if item in common:
            common[item] += 1
        else:
            common[item] = 1
    topn = sorted(common.items(), key=lambda x: x[1], reverse = True)

    return topn



if __name__ == "__main__":
    TotalLines, maleLines, femaleLines = mergeAllDataFiles()
    Best, Worst = sentimentalayisis(maleLines, femaleLines)
    print(Best)
    print(Worst)
    topn = topdescriptions(TotalLines)
    for i in range(10):
        print(topn[i])
