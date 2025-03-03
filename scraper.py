import requests
from bs4 import BeautifulSoup
import json

# 取得するメーカーのURL（例：BANDAI）
URL = "https://bsp-prize.bandainamco-am.co.jp/item/"

def get_figure_data():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    figures = []
    for item in soup.select(".item_list .item"):
        title = item.select_one(".title").text.strip()
        date = item.select_one(".date").text.strip() if item.select_one(".date") else "不明"
        
        figures.append({"title": title, "release_date": date})

    return figures

# データを取得して保存
figures = get_figure_data()
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(figures, f, ensure_ascii=False, indent=4)
