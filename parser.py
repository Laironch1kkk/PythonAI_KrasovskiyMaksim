from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soap_list_href = soup.find-all("a", {"class":"short-img img-fit"})
f = open("link.txt", encoding="utf-8")
for href in soup_list_href:
    f.write(f"{href.text}\n")

f.close()