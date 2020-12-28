import time

from bs4 import BeautifulSoup

from crawcron.conf.conf_op import write_update
from crawcron.conf.mysql_config import insert_db
from crawcron.utils import get_content

def parse_elecfans():
    html = get_content("http://www.elecfans.com/tags/ai/")
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('div.ltctn-wrap>div.info-list.clearfix')
    success_num = 0
    try:
        for table in tables:
            try:
                a = table.select_one('a')
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
            write_update('conf/conf.json', "elecfans" , success_num)
            print(f'elecfans更新了{success_num}篇文章。')


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.select_one('span.time')
    date = date.get_text().strip().split()[0]
    h1 = soup.select_one('h1.article-title')
    title = h1.get_text()
    article_content = soup.select_one('.simditor-body.clearfix')
    content = article_content.get_text().replace("\'","")
    source='elecfans'
    field = 'AI'
    #print(title, content, url, field, date,source)
    return insert_db((title, content, url, field, date,source))


if __name__ == '__main__':
    parse_elecfans()
    pass
