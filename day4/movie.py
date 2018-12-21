import webbrowser
from bs4 import BeautifulSoup
import requests


KEY = "4091f8e0a558552a3064d094f479ff3f"
# base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.xml"
base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleInfo.xml"
peopleCd = 20111111
url =  f"{base_url}?key={KEY}&peopleCd={peopleCd}"
# date = "20180310"

# 1. 요청
print(url)
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
print(soup)
# name = soup.
