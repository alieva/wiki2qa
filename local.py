import json
import csv
import os
from difflib import SequenceMatcher

threshold = 1.0

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

squadTitles = []

with open('data/train-v1.1.json') as file:
    data = json.load(file)
    for root in data['data']:
        title = root['title'].replace("_", " ")
        squadTitles.append(title)

pathToWikiFiles = "../../../var/xdolez52/Zpracování Wikipedie/html_from_wikipedia_en_all_novid_2018-10.zim/6-mg4j"
wikiFiles = os.listdir(pathToWikiFiles)
excluded = ["old-2019-01-12", "old-2019-10-15", "old-2019-10-18", "old-2019-11-20", "old-2019-12-07", "old-2019-11-14", "old-2020-01-02", "fixBadDecodedLinks.py", "missing_entities.py", "missing_entities_2020-01-02.txt", "time-missing_entities_2020-01-02.txt", "time-wikipedia_processing_2020-01-02.txt"]

something_useful = True

print(wikiFiles)

something_more_useful = True

with open('data/output.tsv', mode='a') as output_file:
    output_writer = csv.writer(output_file, delimiter='\t')
    output_writer.writerow(["######### BEGIN #########"])
    for file in wikiFiles:
        if (file not in excluded):
            with open(pathToWikiFiles + "/" + file) as wiki:
                data = csv.reader(wiki, delimiter='\t')
                for t in data:
                    if len(t) > 0:
                        f = t[0]
                        if f.startswith("%%#PAGE"):
                            title = f[8:]
                            for squadTitle in squadTitles:
                                similarity = similar(squadTitle, title)
                                if similarity >= threshold:
                                    match = {"match_percentage": '{0:.2f}'.format(similarity), "squad":squadTitle, "wiki": title, "file": file}
                                    print(match["match_percentage"] + " match: " + match["squad"] + "<=>" + match["wiki"] + file)
                                    output_writer.writerow([match["match_percentage"], match["squad"], match["wiki"], match["file"]])

print("end.")