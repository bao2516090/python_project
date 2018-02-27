# -*- coding:utf-8 -*-
# 关于文件IO输入输出的学习

# 1.文件访问迭代
# 1.1 使用readlines()实现访问文件(有多余换行)
# f = open("C:\python_project\python-unittest\Logging\logging.conf","r")
# lines = f.readlines()
# for line in lines:
#     print(line,)
# f.close()

# 1.2 使用文件迭代实现访问(无多余换行，加了end参数)
# f = open("C:\python_project\python-unittest\Logging\logging.conf","r")
# for line in f:
#     print(line, end="")
# f.close()

# 1.3 使用文件迭代实现访问(无多余换行，加了strip()函数)
# f = open("C:\python_project\python-unittest\Logging\logging.conf","r")
# for line in f:
#     line = line.strip("\n")
#     print(line)
# f.close()

# 2. 文件过滤，显示一个文件的所有行，忽略以井号开头的行(两种做法)
# f = open("C:/python_project/python-unittest/basic_coding/text","r")
# for line in f:
#     if line[0]=='#':
#         # continue
#         line = f.__next__()
#     print(line,end="")
# f.close()

# 3. 文件访问，提示输入数字N和文件F，然后显示文件F的前N行
# filename,len=input("Please input file name and line's length:").split()
# f = open(filename,"r")
# lines = f.readlines()
# for i in range(0,int(len)):
#     print(lines[i],end="")

# 4. 文件访问 输入一个文件名，每次显示文本的10行，暂停并向用户提示"按任意键继续"，按键后继续进行
# filename = input("Please input file name and line's length:")
# f = open(filename, "r")
# lines = f.readlines()
# sum = 0
# for i in lines:
#     print(i, end="")
#     sum += 1
#     if sum == 10:
#         input("按任意键继续: ")
#         sum = 0

# 5.文件比较，写一个比较两个文本文件的程序，如果不同，给出第一个不同的行号和列号
# filenameA, filenameB = input("请输入你要比较的两个文件名称: ").split()
# fa = open(filenameA, "r")
# fb = open(filenameB, "r")
# fa_lines = fa.readlines()
# fb_lines = fb.readlines()
# k = 1
# a_len = len(fa_lines)
# b_len = len(fb_lines)
# min_len = min(a_len, b_len)
# for i in range(0,min_len) :
#     if fa_lines[i] != fb_lines[i]:
#         min_raw_len=min(len(fa_lines[i]),len(fb_lines[i]))
#         for j in range(0,min_raw_len):
#             if fa_lines[i][j] != fb_lines[i][j]:
#                 print("行号是: %d,列号是: %d" % (k,j+1))
#                 break
#     k += 1

# 模块研究 待定
# filename = input("请输入你要查看的模块名称: ")
# module = __import__(filename)
# modules = dir(module)
# print(modules)

# 6.进入到Python标准库目录，检查每个.py文件看是否有__doc__字符串，如果有就对其整理归类。
# 第一步: 找出该目录下所有的文件
import os
str = "C:/Python33/Lib"
num = []
def find_file(dirname):
    for i in os.listdir(dirname):
        if os.path.isdir(dirname + "/" + i):
            find_file(dirname+"/"+i)
        else:
            num.append(dirname+"/"+i)
find_file(str)
file_has_doc = open("hasdoc.txt","a+")
file_has_not = open("nodoc.txt","a+")

doc_lines =""
hasDoc = False
for i in num:
    file = open(i)
    for line in file:
        #如果是刚开始且是以"""开头的 那么就是doc的文件
        if not hasDoc and line.startswith('"""'):
            hasDoc = True
        elif hasDoc and line.startswith('"""'):
            hasDoc = False
            doc_lines +=line
            break
        if hasDoc:
            doc_lines +=line
        else:
            break
    if doc_lines !="":
        file_has_doc.write("文件名: "+ i + "\n")
        file.write("__doc__is: " + doc_lines + "\n")
    else:
        file_has_not.write("文件名" + i + "\n")
    doc_lines = ""
    file.close()

file_has_doc.close()
file_has_not.close()