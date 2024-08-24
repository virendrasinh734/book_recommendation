from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
book_data={}
# Load your title_to_isbn dictionary from the JSON file
json_file_path = 'title_to_isbn_mapping.json'

with open(json_file_path, 'r') as json_file:
    title_to_isbn = json.load(json_file)

driver = webdriver.Chrome()
def scrape_and_save_descriptions(title, isbn_list):
    descriptions = {}
    for isbn in isbn_list:
        url = f"https://openlibrary.org/isbn/{isbn}"
        driver.get(url)
        try:
            read_more_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Read more')
            read_more_link.click()
            time.sleep(2)  # Wait for the description to load
        except:
            pass

        # Find the description element
        description_element = driver.find_element(By.CSS_SELECTOR, '.book-description')

        # Extract the description
        description = description_element.text.strip()
        
        if description and "This edition doesn't have a description yet" not in description:
            descriptions[isbn] = description
            return description
            break

    return "Not found"
permanent_index=0
# Iterate through your title_to_isbn dictionary
for book_title, isbn_list in title_to_isbn.items():
    description = scrape_and_save_descriptions(book_title, isbn_list)
    
    book_data[permanent_index] = {'title': book_title, 'isbns': isbn_list, 'descriptions': description}
    
    filename = f"./descs/{permanent_index}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(description)
    # Increment the permanent index
    permanent_index += 1


driver.quit()

with open("book_data.json", 'w', encoding='utf-8') as json_file:
    json.dump(book_data, json_file, ensure_ascii=False, indent=4)