import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time
books = build('books', 'v1', developerKey='AIzaSyDwDvJt0fU_X_Ct2-8_j2D9NFRXtEzzMW0')

with open('title_to_isbn_mapping.json', 'r') as json_file:
    data = json.load(json_file)

book_info = {}
index = 0

for title, isbns in data.items():
    book_info[index] = {'title': title, 'description': 'Description not available','isbns':isbns}
    index+=1

with open('book_info.json', 'w') as json_output:
    json.dump(book_info, json_output,indent=4)

print('Descriptions saved successfully.')