# -*- coding:utf-8 -*-

import os
# 1.获取执行文件当前路径以及当前路径下的文件
# print(os.getcwd())
# print(os.listdir(os.getcwd()))

# 2.os.path比较重要，用于文件属性的获取
# 2.1 os.path.abspath(path) 获取path的绝对路径
# print(os.path.abspath("os.py"))

# 2.2 os.path.exists(path): 判断文件或者目录是否存在
# print(os.path.exists("bao_log.py"))

# 2.3 os.path.getsize(path): 查看文件或者目录的大小
# print(os.path.getsize("os.py"))

# 2.4 os.path.dirname(path): 返回path的目录
# print(os.path.dirname("C:/tmp/os.py"))

# 2.5 os.path.split(path) :将path分割成目录和文件二元组返回
# print(os.path.split("C:/tmp/os.py"))

# 2.6 os.path.basename(path): 返回path最后的文件名
# print(os.path.basename("C:/tmp/os.py"))

# 2.7 os.path.isfile(path): 判断给定的是否是一个文件
# print(os.path.isfile("C:/python_project/python-unittest/basic_coding/os.py"))

# 2.8 os.path.isdir(path): 判断给定的是否是目录
print(os.path.isdir("C:/python_project"))

