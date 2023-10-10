from googleapiclient.discovery import build
import googleapiclient
from googleapiclient import discovery
# Initialize the Google Books API client
books = build('books', 'v1', developerKey='AIzaSyDwDvJt0fU_X_Ct2-8_j2D9NFRXtEzzMW0')

# Define the ISBN you want to search for
isbn = '9780552152679'

# Perform the ISBN search
response = books.volumes().list(q=f'isbn:{isbn}').execute()

# Extract information about the book(s) from the response
items = response.get('items', [])

if items:
    for item in items:
        # Extract and display the book's description
        volume_info = item.get('volumeInfo', {})
        description = volume_info.get('description', 'Description not available')
        print(f'Description: {description}')
else:
    print('No books found with the given ISBN.')
