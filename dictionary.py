import json
import csv
import os
# from joblib import Parallel, delayed


def nlp(match):
    print(match["match_percentage"] + " match: " + match["squad"] + " " + match["file"])
    print(match["squad_data"])


def do(wiki_file):
    found = False;
    with open(pathToWikiFiles + "/" + wiki_file) as wiki:
        data = csv.reader(wiki, delimiter='\t')
        for t in data:
            if len(t) > 0:
                f = t[0]
                if f.startswith("%%#PAGE"):
                    wiki_title = f[8:]
                    if wiki_title in squad_dictionary:
                        found = True
                        match = {"match_percentage": '{0:.2f}'.format(1),
                                 "squad": wiki_title,
                                 "file": wiki_file,
                                 "squad_data": squad_dictionary[wiki_title]}
                        nlp(match)
        if not found:
            print("no matches found in: " + wiki_file)


squad_dictionary = {}

with open('data/train-v1.1.json') as file:
    squadData = json.load(file)
    for root in squadData['data']:
        title = root['title'].replace("_", " ")
        squad_dictionary[title] = root

pathToWikiFiles = "/var/xdolez52/Zpracování Wikipedie/html_from_wikipedia_en_all_novid_2018-10.zim/6-mg4j"
wikiFiles = os.listdir(pathToWikiFiles)
excluded = ["old-2019-01-12", "old-2019-10-15", "old-2019-10-18", "old-2019-11-20", "old-2019-12-07", "old-2019-11-14", "old-2020-01-02", "fixBadDecodedLinks.py", "missing_entities.py", "missing_entities_2020-01-02.txt", "time-missing_entities_2020-01-02.txt", "time-wikipedia_processing_2020-01-02.txt"]
noMatches = ["wikipedia_en_all_novid_2018-10.htmldump.part0348.vert.parsed.mg4j"]
for ex in excluded:
    wikiFiles.remove(ex)
for nm in noMatches:
    wikiFiles.remove(nm)

#print(wikiFiles)

# Parallel(n_jobs=1)(delayed(do)(file) for file in wikiFiles)
for file in wikiFiles:
    do(file)

print("end.")
