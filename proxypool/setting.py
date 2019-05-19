"""
@Time : 2019/5/14 下午5:09
@Author : kongwiki
@File : setting.py
@Email : kongwiki@163.com 
"""
# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数初始设置
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API
TEST_URL = 'https://weixin.sogou.com/weixin?type=2&query=健康'

# API配置
API_HOST = 'localhost'
API_PORT = 5002

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
