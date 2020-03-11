import pysftp
import os

myHostname = "minerva3.fit.vutbr.cz"
myUsername = "xaliye02"
myPassword = "ha5tertujo"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection successfully established ... ")
    sftp.cwd('/var/xdolez52/Zpracovani_Wikipedie/html_from_wikipedia_en_all_novid_2018-10.zim/6-mg4j')

    items = sftp.listdir()
    excluded = ["fixBadDecodedLinks.py", "missing_entities.py", "missing_entities_2020-01-02.txt", "time-missing_entities_2020-01-02.txt", "time-wikipedia_processing_2020-01-02.txt"]

    wikiFiles = []
    for item in items:
        if sftp.isfile(item) and (item not in excluded):
            wikiFiles.append(item)

    print(wikiFiles)
