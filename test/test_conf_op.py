from crawlcron.conf.conf_op import write_update, read_last_updated, clear
from crawlcron.jiqizhixin import JI_QI_ZHI_XIN

conf = '../conf/conf.json'


def test_write_update():
    write_update(conf, JI_QI_ZHI_XIN, 5)


def test_read_last_updated():
    print(read_last_updated(conf))


if __name__ == '__main__':
    # test_write_update()
    # test_read_last_updated()
    clear(conf)
