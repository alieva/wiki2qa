import json
import csv
import os
from difflib import SequenceMatcher
import pysftp

threshold = 0.92

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


squadTitles = []

with open('data/output.tsv', mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter='\t')
    with open('data/train-v1.1.json') as file:
        data = json.load(file)
        for root in data['data']:
            title = root['title'].replace("_", " ")
            squadTitles.append(title)

myHostname = "minerva3.fit.vutbr.cz"
myUsername = "xaliye02"
myPassword = ""

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection successfully established ... ")
    sftp.cwd('/var/xdolez52/Zpracování Wikipedie/html_from_wikipedia_en_all_nopic_2019-10.zim/6-mg4j')
    
    items = sftp.listdir()
    excluded = ["fixBadDecodedLinks.py", "missing_entities.py", "missing_entities_2020-01-02.txt", "time-missing_entities_2020-01-02.txt", "time-wikipedia_processing_2020-01-02.txt"]
    
    wikiFiles = []
    for item in items:
        if sftp.isfile(item) and (item not in excluded):
            wikiFiles.append(item)

    print(wikiFiles)

    for file in wikiFiles:
        with sftp.open(file) as wiki:
            data = csv.reader(wiki, delimiter='\t')
            for t in data:
                if len(t) > 0:
                    f = t[0]
                    if f.startswith("%%#PAGE"):
                        title = f[8:]
                        for squadTitle in squadTitles:
                            similarity = similar(squadTitle, title)
                            if similarity > threshold:
                                print(str(similarity) + " match: " + squadTitle + "=>" + title)

print("end.")