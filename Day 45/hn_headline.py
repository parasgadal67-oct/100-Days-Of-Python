import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com"
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.ConnectionError:
    print("NO INTERNET CONNECTION. CHECK YOUR WI-FI!")
except requests.exceptions.Timeout:
    print("REQUEST TIMEDOUT. TRY AGAIN LATER!")
else:
    if response.status_code != 200:
        print("Something went wrong! Status", response.status_code)
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find_all("span", class_="titleline")
        print("==== Hacker News - Top Headlines ====")
        for number, title in enumerate(titles, start= 1):
            link = title.find("a")
            print(f"{number}. {link.text}")