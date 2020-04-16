import json
import csv
import os
from included import wikiFiles
from difflib import SequenceMatcher

class Page:
    def __init__(self, title):
        self.title = title
        self.paragraphs = []

class Paragraph:
    def __init__(self, title):
        self.title = title
        self.sentences = []

def listToString(s):
    str1 = ""
    for element in s:
        str1 += " " + element
    return str1

def similarity(a, b):
    print (a,b)
    return SequenceMatcher(None, a, b).ratio()

def do(wiki_file):
    found = False;
    inSquad = False;
    matches = []
    pages = []
    inSentence = False;
    paragraphId = -1
    with open(pathToWikiFiles + "/" + wiki_file) as wiki:
        data = csv.reader(wiki, delimiter='\t')
        for t in data:
            if len(t) > 0:
                f = t[0]
                if f.startswith("%%#PAGE"):
                    wiki_title = f[8:]
                    if wiki_title in squad_dictionary:
                        squad_paragraph = []
                        squad_question = squad_dictionary[wiki_title]
                        for p in squad_question["paragraphs"]:
                            squad_paragraph = p["context"]
                            print(squad_paragraph)

                        inSquad = True
                        found = True
                        match = {"match_percentage": '{0:.2f}'.format(1),
                                 "squad": wiki_title,
                                 "file": wiki_file,
                                 "squad_data": squad_dictionary[wiki_title],
                                 "squad_paragraph": squad_paragraph,
                                 "last_paragraph": []}
                        matches.append(match)
                    else:
                        inSquad = False
                elif f.startswith("%%#PAR") and inSquad == True:
                    if (paragraphId > -1):
                        last_paragraph = matches[-1]["last_paragraph"]
                        squad_paragraph = matches[-1]["squad_paragraph"]
                        sim = similarity(last_paragraph, squad_paragraph)

                    matches[-1]["last_paragraph"] = []
                    paragraphId = paragraphId + 1
                    a = 1
                elif f.startswith("%%#SEN") and inSquad == True:
                    inSentence = True
                elif f.startswith("%%#DOC"):
                    inSentence = False
                elif inSentence == True and inSquad == True:
                    matches[-1]["last_paragraph"].append(t[1])
        if not found:
            print("no matches found in: " + wiki_file)

    return matches


squad_dictionary = {}

with open('data/train-v1.1.json') as file:
    squadData = json.load(file)
    for root in squadData['data']:
        title = root['title'].replace("_", " ")
        squad_dictionary[title] = root


pathToWikiFiles = "/var/xdolez52/Zpracovani_Wikipedie/html_from_wikipedia_en_all_novid_2018-10.zim/6-mg4j"

with open('data/map_paragraphs.tsv', mode='a') as output_file:
    output_writer = csv.writer(output_file, delimiter='\t')
    output_writer.writerow(["######### BEGIN #########"])
    for file in wikiFiles:
        results = do(file)
        for result in results:
            output_writer.writerow([result["match_percentage"], result["squad"], result["file"]])

print("end.")
