# -*- coding: utf-8 -*-
import os

port = 8000
lqr = ['python', 'c++', 'java', 'php', 'ios']
# hello = {
#     'a': 1, 'b': 2, 'c': 3
# }
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置一个settings字典，将所有的配置参数都放到这里,
# 之所以这样配置，是为了定义一些其他的参数
# config与templates在同一级目录时可以这样操作
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),  # 配置模板路径
    'debug': True,  # 开启调试模式
}
"""1
# 当天文件所在路径
print os.path.dirname(__file__)
# 项目的绝对路径
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 不太严谨的写法
print os.path.dirname(os.path.dirname(__file__))
"""
