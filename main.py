import requests
import json
from flask import Flask
text=requests.get('https://www.google.com').text
print(text)