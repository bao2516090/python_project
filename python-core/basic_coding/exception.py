# -*- coding:utf-8 -*-
# 1.try-except语句(比较不加异常处理和加入异常处理的区别)

# f = open("123","r")

# try:
#     f = open("123","r")
# except FileNotFoundError as e:
#     print("找不到相应的文件:",e)
#
# print("continue")

# 2. 编写安全的float()函数(尝试多个except子句)
# def safe_float(obj):
#     try:
#         result = float(obj)
#     except ValueError as e:
#         result = "float函数不能转换非数字的数值"
#     except TypeError as e:
#         result = "float函数不接受非法类型参数"
#     return result
#
# print(safe_float("123"))
# print(safe_float("foo"))
# print(safe_float(["foo"]))

# 3. 处理多个异常的except子句
# def safe_float(obj):
#     try:
#         result = float(obj)
#     except (ValueError,TypeError) as e:
#         result = "非法参数"
#         print(e)
#     return result
#
# print(safe_float("123"))
# print(safe_float("foo"))
# print(safe_float(["foo"]))

# 4.异常参数

# 5.else语句
# def safe_float(obj):
#     try:
#         result = float(obj)
#     except ValueError as e:
#         result = "非法参数"
#         print(e)
#     else:
#         print("no ValueError occur!")
#     return result
#
# print(safe_float("123"))
# print(safe_float("foo"))

# 6. finally子句
# file = None
# try:
#     file = open("tmp1.txt","r")
#     lines = file.readlines()
# except IOError:
#     print("不能打开这个文件")
# finally:
#     if file:
#         file.close()

# 7. raise抛出异常
try:
    s = None
    if s is None:
        raise NameError("None error")
    print("I am here") # 这行代码不会执行
except NameError:
    print("Name error occur")



