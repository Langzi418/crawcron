#
import json
import time

from crawlcron.conf.mysql_config import select_db


def write_update(conf, source, num):
    """

    :param conf: 配置文件路径
    :param source: 爬取来源
    :param num: 更新数量
    :return: 无
    """
    if num == 0:
        return
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)
    data['updated'] += num
    src_dic = data['sources'][source]
    src_dic['last'] = str(time.time())
    src_dic['updated'] += num
    with open(conf, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)


def read_last_updated(conf):
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)
    updated = data['updated']
    if updated == 0:
        return {}

    return_dic = {}
    sources = data['sources']
    for source in sources:
        updated_article = []
        updated = sources[source]['updated']
        if updated > 0:
            results = select_db(source, updated)
            for res in results:
                article = {
                    'title': res[1],
                    'content': res[2],
                    'url': res[3],
                    'field': res[4],
                    'date': res[5]
                }
                updated_article.append(article)
                return_dic[source] = updated_article
    return return_dic


# 重置conf.json
def clear(conf):
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)

    data['updated'] = 0
    tables = data['sources']
    for table in tables:
        tables[table]['last'] = ''
        tables[table]['updated'] = 0

    with open(conf, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)

