import sys
import requests
from bs4 import BeautifulSoup
import os
import time
# f_name=sys.argv[1]
# strart_no=sys.argv[2]
# end_no=sys.argv[3]
# isbn_list=[]
# with open("isbn_names.txt","r") as file:
#     for item in file.readlines():
#         isbn=item.strip()
#         isbn_list.append(isbn)
# print(isbn_list)
# curr_lst=isbn_list[strart_no:end_no]
output_directory = "descriptions"

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
curr_lst=['0002005018', '0374157065', '0399135782', '1552041778', '1558746218', '0440234743', '0452264464', '0609804618', '1841721522', '0971880107', '0345402871']
for isbn in curr_lst:
    description = fetch_book_description(isbn)
    if description:
        filename = f"{isbn}.txt"
        with open(os.path.join(output_directory, filename), "w", encoding="utf-8") as file:
            file.write(description)
            print(f"Saved description for ISBN {isbn} to {filename}")
    else:
        print(f"Description not found for ISBN {isbn}")
    time.sleep(0.5)

print("Done")
