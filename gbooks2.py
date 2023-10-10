from googleapiclient.discovery import build
import googleapiclient
from googleapiclient import discovery
books = build('books', 'v1', developerKey='')

isbn = '9780552152679'

response = books.volumes().list(q=f'isbn:{isbn}').execute()

items = response.get('items', [])

if items:
    for item in items:
        volume_info = item.get('volumeInfo', {})
        description = volume_info.get('description', 'Description not available')
        print(f'Description: {description}')
else:
    print('No books found with the given ISBN.')
