import requests

text=requests.get('https://www.google.com').text
print(text)