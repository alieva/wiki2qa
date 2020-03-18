import os
import csv   

# cur = os.listdir("")
# print(cur) 


with open("data/map.tsv") as wikifilename:
    files = []
    data = csv.reader(wikifilename, delimiter='\t')
    for t in data:
        if len(t) > 2:
            files.append(t[2])

    distinct = set(files)
    for d in distinct:
        print("\"" + d + "\",")
