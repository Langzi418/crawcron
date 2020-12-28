import time

import requests
from bs4 import BeautifulSoup

from crawcron.conf.conf_op import write_update
from crawcron.conf.mysql_config import insert_db
from crawcron.utils import get_content

def parse_qbitai():
    html = get_content("https://www.qbitai.com/")
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('div.picture_text')
    success_num = 0
    try:
        for table in tables:
            try:
                a = table.select_one('h4 a')
                url = a['href']
                print(url)
                if parse_detail(get_content(url), url):
                    success_num += 1
                else:
                    break
                time.sleep(2)
            except Exception as e:
                pass
    finally:
        if success_num > 0:
            write_update('conf/conf.json', "qbitai" , success_num)
            print(f'qbitai更新了{success_num}篇文章。')


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.select_one('.date')
    date = date.get_text()
    h1 = soup.select_one('.article > h1')
    title = h1.get_text()
    article_content = soup.select('.article>p')
    content=''
    for p in article_content:
        content += p.get_text().replace("\'","")
    source='qbitai'
    field = 'AI'
    return insert_db((title, content, url, field, date,source))


if __name__ == '__main__':
    parse_qbitai()
    pass
