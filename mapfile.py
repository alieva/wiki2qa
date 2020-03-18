import json
import csv
import os
from excluded import excluded
from excluded import noMatches
# from joblib import Parallel, delayed


def nlp(match):
    print(match["match_percentage"] + " match: " + match["squad"] + " " + match["file"])
    print(match["squad_data"])


def do(wiki_file):
    found = False;
    matches = []
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
                        matches.append(match)
        if not found:
            print("no matches found in: " + wiki_file)

    return matches


squad_dictionary = {}

with open('data/train-v1.1.json') as file:
    squadData = json.load(file)
    for root in squadData['data']:
        title = root['title'].replace("_", " ")
        squad_dictionary[title] = root

pathToWikiFiles = "/var/xdolez52/Zpracování Wikipedie/html_from_wikipedia_en_all_novid_2018-10.zim/6-mg4j"
wikiFiles = os.listdir(pathToWikiFiles)

for ex in excluded:
    wikiFiles.remove(ex)
for nm in noMatches:
    wikiFiles.remove(nm)

# print(wikiFiles)
with open('data/map.tsv', mode='a') as output_file:
    output_writer = csv.writer(output_file, delimiter='\t')
    output_writer.writerow(["######### BEGIN #########"])
    for file in wikiFiles:
        results = do(file)
        for result in results:
            output_writer.writerow([result["match_percentage"], result["squad"], result["file"]])
print("end.")
