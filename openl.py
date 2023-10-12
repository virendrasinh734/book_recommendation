import requests
from bs4 import BeautifulSoup
import os
import time
import json

output_directory = "filess"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def fetch_book_description(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        description_element = soup.find('div', {'class': 'book-description'})

        if description_element:
            description = description_element.get_text(strip=True)
            return description

    return None

def descextract(json_data):
    for index, book_info in json_data.items():
        isbns = book_info.get('isbns', [])
        if not isbns:
            print(f"No ISBN found for book at index {index}")
            continue

        isbn = isbns[0]

        description = fetch_book_description(isbn)
        if description:
            filename = f"{index}.txt"
            with open(os.path.join(output_directory, filename), "w", encoding="utf-8") as file:
                file.write(description)
                print(f"Saved description for ISBN {isbn} at index {index} to {filename}")
        else:
            print(f"Description not found for ISBN {isbn} at index {index}")
        time.sleep(0.2)

    print("Done")

with open("ind_to_book.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

descextract(data)