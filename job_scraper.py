from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")