import time

import requests
from bs4 import BeautifulSoup

from crawlcron.conf.conf_op import write_update
from crawlcron.conf.mysql_config import insert_db


def get_abstract():
    cookies = {
        'ahoy_visitor': '6daad725-ba5b-4f28-8a61-4e7a372f524d',
        '_ga': 'GA1.2.1534259563.1599059062',
        'ahoy_visit': '03ba7280-f03b-4bfb-976b-f2e3918dcf7e',
        '_gid': 'GA1.2.63598564.1607243943',
        '_Synced_session': 'JwGVAqK3AabecRlQqKBfl5BAX%2BqYAYGQKaf5Yq5zk1Dfc0ChJcubCnvCPslbua%2BGnaUxW0E6BG%2BRCivyX1PaSuUdKb706XIPFy8r9kWgB2QkoP3m16Ie7z6MfzVhNUMYaYuAMNoYdUJOJfB3Vv7oQR5YvhcvozJTywByshTRN5GbWvOJPt%2BL2gvQUaXOPs8VGzoiY6%2BU7egX7yZcFsV6hGFETIgWXkm%2FctA7fbu87Fy5S77EHkPCeObpmYzzxvDM0AhceJoLgrwTYxA3YNXMvVBZtvHolWxDSw72v2XJv1%2Bt2LosXk%2FetBgS4G3J7hKUp%2Fk5talfpMFXzBYX7kyKGz4%2B4XLmG0WAyt5rJo7yfdej4GaLCA%3D%3D--aISUBrr3E2XRCHmB--2QDF5smVOPjeSnqiJu3eSA%3D%3D',
    }
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.jiqizhixin.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'If-None-Match': 'W/"4895f67d90d58e7d0ae0eaa446bbaafe"',
    }

    response = requests.get('https://www.jiqizhixin.com/', headers=headers)

    return response.text


def get_detail(url):
    cookies = {
        'ahoy_visitor': '6daad725-ba5b-4f28-8a61-4e7a372f524d',
        '_ga': 'GA1.2.1534259563.1599059062',
        'ahoy_visit': '03ba7280-f03b-4bfb-976b-f2e3918dcf7e',
        '_gid': 'GA1.2.63598564.1607243943',
        '_Synced_session': 'HhhK8Ys8%2BFSefqtSCShgvNxJ38a2RuPn1GZxbv5NitS4GJRs88UKYfIvL%2FjI0sOGwuStndqCy%2BS3YNmkj7Ori74euJ%2B%2F7pzsLWzMDC2wl3h6jJ%2BnBhLx7Xxq%2FbyZ%2FkWsbgH88YwSlqdkWyR9hbmt%2FOzUtPSoXxf2N5xmIfDGvTTnymNP%2BAyFKwyQ%2FE49mV3C%2FP%2Ba5n4Du58UV0b1JGugryArAzMGwtwIREFq6w9n7KHjByLY6Hkrm7wMe1LATH%2FDHJB8eWazpwPBmonPADRedWrOqTmFUEmSFP8Kq4J8VUR2weXdBh8L%2Ffj4qfbkVqg%2FCiwXen6fG1mZJflUwstrO8WLBzDQdWzdFjZPyKRRr3QJL2FNQ8w0y%2B9prolD4Ebdi%2FMl3T%2F3VwXoCJTi%2BSEcVGQ%3D--nh9zCZlDUwsHjeaD--Be3%2FrdVaySQkBWNIm2ehVw%3D%3D',
    }
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'If-None-Match': 'W/"debf651895542dafb77525d026710391"',
    }
    response = requests.get(url, headers=headers)
    return response.text


def parse_jiqizhixin():
    html = get_abstract()
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.select('div.u-block__item.js-u-item.is-active > article')
    success_num = 0
    for table in tables:
        a = table.select_one('main > section > a')
        url = 'https://www.jiqizhixin.com' + a['href']
        if parse_detail(get_detail(url), url):
            success_num += 1
        else:
            break
        time.sleep(2)

    if success_num > 0:
        write_update('conf/conf.json', 'jiqizhixin', success_num)
        print(f'机器之心更新了{success_num}篇文章。')


def parse_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    date = soup.select_one('#articles-show > div.article > div > div:nth-child(1) time')
    date = date.get_text()
    h1 = soup.select_one('#articles-show > div.article > div > div:nth-child(1) > h1')
    title = h1.get_text()
    article_content = soup.select_one('#js-article-content')
    content = article_content.get_text()
    field = 'AI'
    return insert_db('ai', 'jiqizhixin', (title, content, url, field, date))


if __name__ == '__main__':
    pass
