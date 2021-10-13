# Packages
import pandas as pd
import json
import csv
import re 
from lyricsTokenizer import tokenizer

# Raw Data
songData_set1 = pd.read_csv("./dataset/raw/songData_set1.csv")
songData_set2 = pd.read_csv("./dataset/raw/songData_set2.csv")

# Processed Data Storage
jsonData = {}
jsonData['songs'] = []
csvData = []
csvHeader = ['Artist', 'Title','Lyrics', 'Genre']

# Data Preparation
# Song Data Set 1
for i in range(0, len(songData_set1)):

    if not re.search("\/",songData_set1.genre[i]):
        tempCSVData = [songData_set1.artist[i], songData_set1.title[i], tokenizer(songData_set1.lyrics[i]), songData_set1.genre[i]]
        csvData.append(tempCSVData)

        tempJSONData = {
            'Artist' : songData_set1.artist[i],
            'Title'  : songData_set1.title[i],
            'Lyrics' : tokenizer(songData_set1.lyrics[i]),
            'Genres' : songData_set1.genre[i],
        }
        jsonData['songs'].append(tempJSONData)

# Song Data Set 2
for i in range(0, len(songData_set2)):

    if not re.search("\/",songData_set2.genre[i]):
        tempCSVData = [songData_set2.artist[i], songData_set2.title[i], tokenizer(songData_set2.lyrics[i]), songData_set2.genre[i]]
        csvData.append(tempCSVData)
        
        tempJSONData = {
            'Artist' : songData_set2.artist[i],
            'Title'  : songData_set2.title[i],
            'Lyrics' : tokenizer(songData_set2.lyrics[i]),
            'Genres' : songData_set2.genre[i],
        }
        jsonData['songs'].append(tempJSONData)


# File Output
with open('./dataset/processed/songList.json', 'w') as outfile:
    json.dump(jsonData, outfile)

with open('./dataset/processed/songList.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvHeader)
    writer.writerows(csvData)