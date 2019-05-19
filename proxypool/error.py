"""
@Time : 2019/5/14 下午5:09
@Author : kongwiki
@File : error.py
@Email : kongwiki@163.com 
"""


class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经用完')
