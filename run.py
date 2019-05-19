"""
@Time : 2019/5/14 下午10:20
@Author : kongwiki
@File : run.py
@Email : kongwiki@163.com 
"""
from proxypool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except:
        main()


if __name__ == '__main__':
    main()