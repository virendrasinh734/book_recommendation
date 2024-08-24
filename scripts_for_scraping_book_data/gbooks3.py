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
    book_info[index] = {'title': title, 'description': 'Description not available'}

    for isbn in isbns:
        try:
            response = books.volumes().list(q=f'isbn:{isbn}').execute()
            items = response.get('items', [])
            if items:
                item = items[0]
                volume_info = item.get('volumeInfo', {})
                description = volume_info.get('description', 'Description not available')
                book_info[index]['description'] = description
                break  
        except HttpError as e:
            if e.resp.status == 404:
                print(f'Book not found for ISBN: {isbn}')
            else:
                print(f'Error fetching book info for ISBN: {isbn}, Error: {str(e)}')

    with open(f'./ddeess/{index}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(book_info[index]['description'])
    index += 1  
    time.sleep(1)

with open('book_info.json', 'w') as json_output:
    json.dump(book_info, json_output)

print('Descriptions saved successfully.')