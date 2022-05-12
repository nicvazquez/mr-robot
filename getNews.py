import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

url = "https://www.xataka.com/"
def getNews():
    answer = requests.get(url, headers = headers)
    soup = BeautifulSoup(answer.text, "html.parser")

    title = soup.find("h2", itemprop="headline").text
    description = soup.find("div", itemprop="description").text
    link = soup.find("div", itemprop="description").find("a")["href"]

    message = f"""
    **{title}**
    {description} {link}
    """

    return message
