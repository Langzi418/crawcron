#
import json
import time

from crawlcron.conf.mysql_config import select_db


def write_update(conf, src, num):
    if num == 0:
        return
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)
    data['updated'] += num
    src_dic = data['tables'][src]
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
    tables = data['tables']
    for table in tables:
        updated_article = []
        updated = tables[table]['updated']
        if updated > 0:
            results = select_db('ai', table, updated)
            for res in results:
                article = {
                    'title': res[1],
                    'url': res[2],
                    'time': res[3],
                    'content': res[4]
                }
                updated_article.append(article)
                return_dic[table] = updated_article
    return return_dic


# 重置conf.json
def clear(conf):
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)

    data['updated'] = 0
    tables = data['tables']
    for table in tables:
        tables[table]['last'] = ''
        tables[table]['updated'] = 0

    with open(conf, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    # write_update('jiqizhixin', 10)
    # read_last_updated('conf.json')
    clear('conf.json')
