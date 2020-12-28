#
import time
import schedule

from crawcron.jiqizhixin import parse_jiqizhixin
from crawcron.qbitai import parse_qbitai
from crawcron.AItists import parse_AItists
from crawcron.elecfans import parse_elecfans

if __name__ == '__main__':
    # 初始启动时执行一次
    parse_jiqizhixin()
    parse_qbitai()
    parse_AItists()
    parse_elecfans()

    # 以后每隔一段时间执行一次
    schedule.every(2).hours.do(parse_jiqizhixin)
    schedule.every(2).hours.do(parse_qbitai)
    schedule.every(2).hours.do(parse_AItists)
    schedule.every(2).hours.do(parse_elecfans)
    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(10)
