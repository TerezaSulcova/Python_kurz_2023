import json
with open("body.json",mode="r", encoding="utf-8") as soubor:
    body=json.load(soubor)
print(body)

prospech= {}

for student in body:
    if body[student] >= 60:
        prospech[student] = "pass"
    else:
        prospech[student] = "fail"

with open("prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dumps("prospech")
print(prospech)
