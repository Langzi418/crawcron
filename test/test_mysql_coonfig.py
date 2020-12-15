from crawlcron.conf.mysql_config import select_db
from crawlcron.jiqizhixin import JI_QI_ZHI_XIN

if __name__ == '__main__':
    print(select_db(JI_QI_ZHI_XIN, 100))
