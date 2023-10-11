import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time
import logging
# log_file_path = "./logs/log_file5.txt"
logging.basicConfig(filename="process_9_n.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
books = build('books', 'v1', developerKey='')  

with open('.\jsons\part_9.json', 'r') as json_file:
    data = json.load(json_file)

book_info = {}
index = 7680

for entry in data:
    inner_dict = entry[str(index)]
    title = inner_dict['title']
    isbns = inner_dict['isbns']

    book_info[index] = {'title': title, 'description': 'Description not available'}
    for isbn in isbns:
        try:
            response = books.volumes().list(q=f'isbn:{isbn}').execute()
            items = response.get('items', [])
            if items:
                item = items[0]
                volume_info = item.get('volumeInfo', {})
                description = volume_info.get('description', 'Description not available')
                categories = volume_info.get('categories', [])
                book_info[index]['description'] = description
                book_info[index]['categories'] = categories
                logging.info(f'Book info found for ISBN: {isbn} , title:{title}') 
                break
        except HttpError as e:
            if e.resp.status == 404:
                logging.error(f'Book not found for ISBN: {isbn}')
                print(f'Book not found for ISBN: {isbn}')
            else:
                logging.error(f'Error fetching book info for ISBN: {isbn}, Error: {str(e)}')
                print(f'Error fetching book info for ISBN: {isbn}, Error: {str(e)}')

    with open(f'./ddeess/{index}.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(book_info[index]['description'])
        logging.info(f'Data written to file for index: {index}')
    index += 1
    time.sleep(1)
ofname='book_info_9_n.json'
with open(ofname, 'w') as json_output:
    json.dump(book_info, json_output,indent=4)
    logging.info(f"Book info dictioanry dumped to a json: {ofname}")

print('Descriptions saved successfully.')
