from jsonStripper import *
from striphtml import *
from cosine import *
import codecs

infile = 'data.json'
result = JSON_stripper(infile)

strippedResult = list()

for question in result:
    strippedResult.append(HTML_stripper(question))
    
print len(strippedResult)

similarGrouped = { i: [] for i in range(len(strippedResult)+1)}
print len(similarGrouped)
#exit(0)
    
#print strippedResult[]

#fo = codecs.open("outfile.txt", "w", "utf-8")

#for text in strippedResult:
#    fo.write(text)


def grouper():
    groupCount = -1
    for q in strippedResult:
        #print similarGrouped
        foundSimilar = 0
        for i, groupQ in (similarGrouped).items():
            if(groupQ!=[]):
                c = cosineValue(groupQ[0], q)
                
                if(c > 0.95):
                    foundSimilar = -1
                    break
                elif(c > 0.70):
                    foundSimilar = 1
                    similarGrouped[i].append(q)
                    break
            else:
                break
        if(foundSimilar == 0):
            groupCount+=1
            similarGrouped[groupCount].append(q)
            

grouper()
print similarGrouped
def similar(question):
    print question+u'\n'
    for q in strippedResult:
        if(cosineValue(question, q) > 0.60):
            print q+u'\n'
            
#similar(strippedResult[23])
