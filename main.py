import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com"
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# Find the specific HTML tag and extract its text
tag = soup.find("input", {"class": "password-display"})
my_string = tag.text

# Print the string
print(my_string)
