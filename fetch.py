import requests
from bs4 import BeautifulSoup
import os


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

for isbn in isbns:
    description = fetch_book_description(isbn)
    if description:
        filename = f"{isbn}.txt"
        with open(os.path.join(output_directory, filename), "w", encoding="utf-8") as file:
            file.write(description)
            print(f"Saved description for ISBN {isbn} to {filename}")
    else:
        print(f"Description not found for ISBN {isbn}")

print("Done")
