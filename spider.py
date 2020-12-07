#
import time

import schedule

from crawlcron.jiqizhixin import parse_jiqizhixin

if __name__ == '__main__':
    # 初始启动时执行一次
    parse_jiqizhixin()

    # 以后每隔一段时间执行一次
    # https://zhuanlan.zhihu.com/p/92152648
    schedule.every(2).hours.do(parse_jiqizhixin)
    while True:
        schedule.run_pending()  # 运行所有可以运行的任务
        time.sleep(10)
