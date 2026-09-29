import csv
import json
from textwrap import indent

with open('resume.json','r') as file:
    resume = json.load(file)
    with open ('new_resume.json','w') as file_1:
        json.dump(resume,file_1,indent=2)
data=json.load(open('resume.json'))

for item in data:
    print(data["skills"][1])
