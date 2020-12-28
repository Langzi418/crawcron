import json
import time

from crawcron.conf.mysql_config import select_db


def write_update(conf, src, num):
    if num == 0:
        return
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)
    #总共更新
    data['updated'] += num
    #来源
    src_dic = dict()
    #最后更新时间
    src_dic['last'] = str(time.time())
    #本来源最后更新数目
    src_dic['updated'] = num
    data['src'][src] = src_dic
    with open(conf, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)


def read_last_updated(conf):
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)
    updated = data['updated']
    if updated == 0:
        return {}
    return_dic = {}
    src = data['src']
    for s in src:
        updated_article = []
        updated = src[s]['updated']
        if updated > 0:
            results = select_db(updated,s)
            for res in results:
                article = {
                    'id':res[0],
                    'title': res[1],
                    'feild': res[4],
                    'time': res[5],
                    'url': res[3],
                    'content': res[2],
                    'source':res[6]
                }
                updated_article.append(article)
                return_dic[s] = updated_article
    return return_dic


# 重置conf.json
def clear(conf):
    with open(conf, encoding='utf-8') as f:
        data = json.load(f)

    data['updated'] = 0
    src = data['src']
    for s in src:
        src[s]['last'] = ''
        src[s]['updated'] = 0
    with open(conf, 'w', encoding='utf-8') as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    write_update('conf.json', "elecfans" , 6)
    # read_last_updated('conf.json')
    #clear('conf.json')
