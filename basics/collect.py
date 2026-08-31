import os
from bs4 import BeautifulSoup

for file in os.listdir("data"):
    if file.endswith(".html"):
        with open(os.path.join("data", file), "r", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "html.parser")

        print(soup.prettify())