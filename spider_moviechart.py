# coding=utf-8
# 豆瓣电影排行榜

import requests
from bs4 import BeautifulSoup

url_base = 'https://movie.douban.com/top250?start='
page = '0'


def get_movie_charts():
    for page in range(0, 250, 25):
        r = requests.get(url_base + str(page))
        print(r)
        soup = BeautifulSoup(r.content, 'html.parser')
        box = soup.find_all('div', class_='item')
        movie = []
        for i in range(len(box)):
            movie += [
                [box[i].div.img['src'], box[i].div.img['alt'], box[i].select('em')[0].text,
                 box[i].select('span')[5].text]]
        chart_session = requests.session()
        for i in movie:
            print(i)
            img = chart_session.get(i[0])
            with open('charts/' + i[2] + "__" + i[1][:20] + '.jpg', 'wb') as f:
                f.write(img.content)
                f.close()
            with open('charts.txt', 'w', encoding='utf-8') as o:
                o.write(i[1])
                o.close()


get_movie_charts()
