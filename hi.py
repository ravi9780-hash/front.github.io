from django.shortcuts import render
from  bs4 import  BeautifulSoup
import  requests
import  csv
import  re

ul = "https://codescracker.com/html/html-structure.htm"
response = requests.get(ul)
soup = BeautifulSoup(response.text, 'html5lib')
print(soup)
