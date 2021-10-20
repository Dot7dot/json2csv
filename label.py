import json
import csv
import pandas as pd

with open('指定檔案.json', 'r', encoding='utf-8') as user_data:
    tweets_data = json.load(user_data)

with open("生成新檔案.csv", "w", newline="", encoding='utf-8') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerow(["id", "physical aggression", "verbal aggression", "anger", "hostility", "content"])
    for f in tweets_data:
        wr.writerow([f['id'], 0, 0, 0, 0, f['content']])

