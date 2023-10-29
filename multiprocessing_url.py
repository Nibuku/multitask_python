import os
import logging
import multiprocessing
import requests
from bs4 import BeautifulSoup


def create_directory(folder: str) -> str:
    """The function takes the path to the folder and it's name,
    checks it's presence.
    In case of absence creates a folder.
    """
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except Exception as ex:
        logging.error(f"Couldn't create folder: {ex.message}\n{ex.args}\n")


def make_list(url: str) -> list:
    """The function accepts a link to a search query.
    Creates a list that contains links to each object
    from all specified request pages.
    """
    list_url = []

    try:
        for pages in range(5):
            url_new = url[:-1]
            url_pages: str = f"{url_new}{pages}"
            html = requests.get(url_pages, headers={
                                "User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(html.text, "lxml")
            flowers = soup.findAll("img", class_="mimg")
            for link in flowers:
                r = link.get("src")
                if r != None:
                    list_url.append(r)
                if r == None:
                    continue
        print(list_url)
        return list_url
    except Exception as ex:
        logging.error(f"uncorrect URL\n")


def download(url: str) -> None:
    """Downloads one image from the link"""
    response = requests.get(url)
    create_directory("image")
    count_files = len(os.listdir("image"))
    with open(os.path.join("image", f"{count_files+1:04}.jpg"), "wb") as file:
        file.write(response.content)


if __name__ == "__main__":
    # https://www.bing.com/images/search?q=memes%20about%20wolves&qs=UT&form=QBIR&sp=1&lq=0&pq=memes%20about%20wol&sc=10-15&cvid=076C5499460E484BA562645C9F98C1DA&first=1
    url = input("Введите ссылку на страницу с изображениями")
    r = make_list(url)
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        p.map(download, r)
