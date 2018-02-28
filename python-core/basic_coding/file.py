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

# 6. python采用wb方式写入
# f = open("C:/tmp/tmp.txt","wb")
# str ="小鲍"
# print(type(str))
# f.write(str.encode("utf8"))
# f.close()

# 7.进入到Python标准库目录，检查每个.py文件看是否有__doc__字符串，如果有就对其整理归类。
# 第一步: 找出该目录下所有的文件
# 第二步: 采用wb的方式建立两个需要写入的文件
# 第三步: 循环遍历每个文件，逻辑判断是否含有__doc__字符串的内容 有内容的加入到doc_lines中
# 第四步: 如果doc_lines有内容，说明需要归类在A文件中，没有内容归类在B文件中
# 难点:
#   1) 如果不采用rb的方式打开，windows上的文件是gbk编码，但是在open指定采用gbk编码打开的时候，显示gbk不能识别其中的字符，很奇怪
#   2) 采用rb方式打开，会以二进制方式打开，形成bytes字节流，注意在写入的时候，也需要将str encode成bytes保存
# import os
# import sys
#
# str = r"C:/Python33/Lib"
#
# num = []
# def find_file(dirname):
#     for i in os.listdir(dirname):
#         if os.path.isdir(dirname + "/" + i):
#             find_file(dirname+"/"+i)
#         else:
#             num.append(dirname+"/"+i)
# find_file(str)
# file_has_doc = open("hasdoc.txt","wb")
# file_has_not = open("nodoc.txt","wb")
#
# doc_lines = b""
# hasDoc = False
#
# for i in num:
#     file = open(i,'rb')
#     for line in file:
#         #如果是刚开始且是以"""开头的 那么就是doc的文件
#         if not hasDoc and line.startswith(b'"""'):
#             hasDoc = True
#         elif hasDoc and line.startswith(b'"""'):
#             hasDoc = False
#             doc_lines += line
#             break
#         if hasDoc:
#             doc_lines = doc_lines + line
#         else:
#             break
#
#     if doc_lines != b"":
#         file_has_doc.write("文件名是: \n".encode("utf8") + i.encode("utf8") + "\n".encode("utf8"))
#     else:
#         file_has_not.write("文件名是: \n".encode("utf8") + i.encode("utf8") + "\n".encode("utf8"))
#     doc_lines = b""
#     file.close()
#
# file_has_doc.close()
# file_has_not.close()

# 8.复制文件,提示输入两个文件名，把第一个文件的内容复制到第二个文件中去
# filename_a,filename_b = input("请输入两个文件名: ").split()
# file_a =open(filename_a,"r")
# file_b = open(filename_b,"w")
# for f in file_a:
#     file_b.write(f)
# file_a.close()
# file_b.close()

# 9.文本处理 人们输入的文字常常超过屏幕的最大宽度，编写一个程序，在一个文件中查找长度大于10个字符的文本行，从最接近80个字符的
# 单词断行，把剩余行插入到下一行处。(需要用到临时的文件)
# filename = input("请输入要处理的文件名称: ")
# file = open(filename,"r")
# tmp_file =open("tmp.txt","w")
# for f in file:
#     if len(f) > 10:
#         list_f = list(f)
#         count = len(list_f) / 10
#         for i in range(0,int(count)):
#             tmp_file.write("".join(list_f[:9]))
#             tmp_file.write("\n")
#             list_f = list_f[9:]
#         tmp_file.write("".join(list_f[:9]))
#     else:
#         tmp_file.write(f)
# file.close()

# 10.搜索文件，输入一个字节值和一个文件名，显示该字符在文件中出现的次数
filename, i = input("请输入要搜索的文件名称和要搜索的字节值: ").split()
file = open(filename,"r")
ch = chr(int(i))

sum = 0
for f in file:
    sum += f.count(ch)

print(sum)





