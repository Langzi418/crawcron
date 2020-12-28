import time

from bs4 import BeautifulSoup

from crawcron.conf.conf_op import write_update
from crawcron.conf.mysql_config import insert_db
from crawcron.utils import get_content

def parse_AItists():
    html = get_content("https://wemp.app/accounts/973991ad-c4de-49a4-a553-96c286116b4b")
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('div.post-item__main')
    success_num = 0
    try:
        for table in tables:
            try:
                a = table.select_one('a')
                url = 'https://wemp.app' + a['href']
                if parse_detail(get_content(url), url):
                    success_num += 1
                else:
                    break
                time.sleep(2)
            except Exception as e:
                pass
    finally:
        if success_num > 0:
            write_update('conf/conf.json', "AItists" , success_num)
            print(f'AItists更新了{success_num}篇文章。')


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.select_one('div.post__date')
    date = date.get_text().strip().split()[0]
    h1 = soup.select_one('h1.post__title')
    title = h1.get_text()
    article_content = soup.select_one('#content')
    content = article_content.get_text().replace("\'","")
    source='AItists'
    field = 'AI'
    return insert_db((title, content, url, field, date,source))


if __name__ == '__main__':
    parse_AItists()
    pass
