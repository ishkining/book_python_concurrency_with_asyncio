import requests

response = requests.get('')

items = response.headers.items()

headers = [f'{key}: {value}' for key, value in items]

formatted_headers = '\n'.join(headers)

with open('headers.txt', 'w') as file:
    file.write(formatted_headers)