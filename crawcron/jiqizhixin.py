import time

from bs4 import BeautifulSoup

from crawcron.conf.conf_op import write_update
from crawcron.conf.mysql_config import insert_db
from crawcron.utils import get_content

def parse_jiqizhixin():
    html = get_content("https://www.jiqizhixin.com")
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('div.u-block__item.js-u-item.is-active > article')
    success_num = 0
    try:
        for table in tables:
            try:
                a = table.select_one('main > section > a')
                url = 'https://www.jiqizhixin.com' + a['href']
                if parse_detail(get_content(url), url):
                    success_num += 1
                else:
                    break
                time.sleep(2)
            except Exception as e:
                pass
    finally:
        if success_num > 0:
            write_update('conf/conf.json', "jiqizhixin" , success_num)
            print(f'机器之心更新了{success_num}篇文章。')


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.select_one('#articles-show > div.article > div > div:nth-child(1) time')
    date = date.get_text().strip().splt(" ")[0]
    h1 = soup.select_one('#articles-show > div.article > div > div:nth-child(1) > h1')
    title = h1.get_text()
    article_content = soup.select_one('#js-article-content')
    content = article_content.get_text().replace("\'","")
    source='jiqizhixin'
    field = 'AI'
    return insert_db((title, content, url, field, date,source))


if __name__ == '__main__':
    parse_jiqizhixin()
    pass
