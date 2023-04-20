import os
import requests
from bs4 import BeautifulSoup as Bs

r = requests.get("http://avdejenko.ru/projects/lectures_list")
html = Bs(r.content, 'html.parser')
items = html.find("div", class_="content_wrap").find("div", class_="audiobook").find("ul")
items = items.find_all("li")
for item in items:
    name = item.find("div", class_="about_book").find("a").get_text().split(".")
    name = [x for x in name if x != '']
    name_2 = name[-1].split(" ")
    name_2 = [x for x in name_2 if x != '']
    del name[-1]
    for i in name_2:
        name.append(i)
    disk = item.find("div", class_="about_book").find("div").find_all("a", class_="button_audio")[1]
    disk = "http://avdejenko.ru" + disk.get("href")
    print(name)
    if len(name) == 2:
        if not os.path.isdir(f"muzik/{name[0]}"):
            os.mkdir(f"muzik/{name[0]}")
        with open(f'muzik/{name[0]}/{name[1]}.mp3', "wb") as f:
            f.write(requests.get(disk).content)
    elif len(name) == 3:
        if not os.path.isdir(f"muzik/{name[0]}"):
            os.mkdir(f"muzik/{name[0]}")
        if not os.path.isdir(f"muzik/{name[0]}/{name[1]}"):
            os.mkdir(f"muzik/{name[0]}/{name[1]}")
        with open(f'muzik/{name[0]}/{name[1]}/{name[2]}.mp3', "wb") as f:
            f.write(requests.get(disk).content)
    elif len(name) == 4:
        if not os.path.isdir(f"muzik/{name[0]}"):
            os.mkdir(f"muzik/{name[0]}")
        if not os.path.isdir(f"muzik/{name[0]}/{name[1]}"):
            os.mkdir(f"muzik/{name[0]}/{name[1]}")
        if not os.path.isdir(f"muzik/{name[0]}/{name[1]}/{name[2]}"):
            os.mkdir(f"muzik/{name[0]}/{name[1]}/{name[2]}")
        with open(f'muzik/{name[0]}/{name[1]}/{name[2]}/{name[3]}.mp3', "wb") as f:
            f.write(requests.get(disk).content)
