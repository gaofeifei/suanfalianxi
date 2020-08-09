#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime
import time
import re
from itertools import product
from itertools import combinations
from itertools import dropwhile
from itertools import islice

def test(nums):
    nums.sort()
    nums.sorted()
    for i,v in enumerate(nums):
        print(i,v)
#获得切片下标，返回切片下标和对应文件内容的list
def slice_up(source_path,capter_name):
    sf = open(source_path, 'r', encoding='utf-8')
    # print(sf.readlines())
    sn_list = [sn.strip() for sn in sf.readlines()]
    # print(sn_list)
    last = len(sn_list)
    # print(last)
    slice_list = []
    for cn in capter_name:
        # print(cn)
        # print(sn_list.index(cn))
        slice_i = sn_list.index(cn)
        slice_list.append(slice_i)
    slice_list.append(last)
    # print(slice_list)
    return slice_list, sn_list

#拆分大文件
def split_file_into_different_files(slice_list, sn_list, cpath_list):
    # print(slice_list)
    # [0, 12, 33, 58, 80, 106, 114, 121, 153, 191]
    last = len(slice_list)
    l = []
    regex = re.compile(r'([0-9]{1,3})\t')#正则找出题目编号
    for z, j in enumerate(slice_list):
        if j == 191:
            break
        # print(sn_list[j:slice_list[z+1]])
        l1 = sn_list[j:slice_list[z + 1]]
        l.append(l1)
    for i, v in enumerate(cpath_list):
        f = open(v, 'w', encoding='utf-8')
        str = "".join(l[i])
        sl = regex.findall(str)
        for q in sl:
            str = str.replace(q+'\t','\n'+q+'\t')
        f.write(str)
        f.close()

#废了 XXX自动写入注释 (准备好 XXXcatalogue.txt 文件内容 例如 算法的题目)
#获得注释
def get_annotation(capter_name1,sn_list, slice_list):
    items = capter_name1
    # print(capter_name1)
    # print(sn_list)
    # print(slice_list)
    # print(items)
    # print(sn_list)
    #过滤函数 过滤list中不需要的元素
    #用集合的性质可以解决，但是返回的结果 是乱序，怎么办
    # l1 = set(items)^set(sn_list)#不重复的元素
    # l2 = set(items)|set(sn_list)
    # l3 = set(items)&set(sn_list)
    # ll = [i for i in sn_list if i not in capter_name1]
    # print(ll)
    # l4 = set(sn_list)-set(items)
    # print(l4)
    for i1 in sn_list:
        if i1 not in capter_name1:
            pass
        else:
            # print(sn_list.index(i1))
            pass

def makefile(path,s,d,bookname,capter_name, capter_name1,sn_list):
    ld = len(d)
    num = 0
    ll = [i for i in sn_list if i not in capter_name1]
    ll.append('end')
    count = 0
    print(ll)
    for root, dirs, files in os.walk(path):
        #print(root)#绝对路径
        # print(dirs)
        for i in dirs:
            sub_path = path+"\\"+i
            if os.path.exists(sub_path):
                # print(sub_path)
                os.chdir(sub_path)#转换路径
                cata = open(i+"catalogue.txt","a+")
                cpath = os.getcwd()#当前目录
                while 1:
                    # print(num)
                    num += 1
                    if num > 0 and num <= ld:
                        # print(num)
                        for j in range(1,s[num-1]+1):
                            # print(str(j)+".py")
                            # filename = str(d[num - 1]) + "." + str(j) + ".py"
                            filename = str(j) + ".py"
                            # print(filename)
                            ccpath= path+"\\"+str(d[num - 1])
                            # print("hahaha:"+ccpath)
                            # print(ccpath+"\\"+filename)#所有文件路径
                            f = open(ccpath+"\\"+filename, 'w+',encoding='utf-8')#直接打开一个文件，如果文件不存在则创建文件
                            # f.write(str(d[num - 1]) + "." + str(j))
                            wline = '"""\nBOOK:'+bookname+"\n"+str(capter_name[num - 1]) + "_第" + str(j)+'题\n'+ll[count]+'\n"""'+'\n'
                            # 200805 beg
                            if count > 183:
                                break
                            count += 1
                            # 200805 end
                            print(wline)
                            f.writelines(wline)
                            f.close()
                    else:
                        break
    # print(num)

if __name__ == '__main__':
    bookname = "python_180_zuo.pdf(程序员代码面试指南整理)"
    path = r'../python_arithmetic/'
    tpath = os.path.realpath(path)  # 绝对路径

    # print(tpath)
    lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    capter_name = ['栈和队列', '链表问题', '二叉树问题', '递归和动态规划', '字符串问题', '大数据和空间限制', '位运算', '数组和矩阵问题', '其他题目']
    lessons_list = [11, 20, 24, 20, 25, 7, 6, 31, 37]
    cl = len(capter_list)
    # print(cl)
    cnamedir_list = []
    cpath_list = []
    relative_list = []
    capter_name1 = ['第 1 章  栈和队列', '第 2 章  链表问题', '第 3 章  二叉树问题', '第 4 章  递归和动态规划', '第 5 章  字符串问题', '第 6 章  大数据和空间限制',
                    '第 7 章  位运算', '第 8 章  数组和矩阵问题', '第 9 章  其他题目']

    for i in range(1, cl + 1):
        cname = str(i) + capter_name[i - 1]
        # print(cname)
        cnamedir_list.append(cname)
        cpath = tpath + '\\' + cname + '\\' + cname + 'catalogue.txt'
        # print(cpath)
        cpath_list.append(cpath)
        relative_path = cname + 'catalogue.txt'
        relative_list.append(relative_path)
    print(cnamedir_list)
    # print(cpath_list)
    source_path = tpath + '\\' + 'python_180zuo.txt'
    # print(source_path)
    # 得到切片文件下标
    slice_list, sn_list = slice_up(source_path, capter_name1)
    # 拆分大文件内容到不同文件里,用来做每一章每个算法题的笔记，可选
    split_file_into_different_files(slice_list, sn_list, cpath_list)
    # 废了获得注释
    # get_annotation(capter_name1, sn_list, slice_list)
    #参数列表:1路径 2每一章多少小节 3编号+章节名称 4书名 5每一章的章节名字 6第i章 每一章的章节名字capter_name1 7对应文件内容的list
    makefile(tpath, lessons_list, cnamedir_list, bookname, capter_name, capter_name1, sn_list)

#——————————————————————————————————————————————————————————————————————————————————————————
    """
    自动生成文件夹文件和注释(例如 第一题 栈和队列_第1题 1	设计一个有 getMin 功能的栈)
    首先设置 1书名，2路径，3章节个数(可以自动生成l = [i for i in range(1,10)])，4每一章多少小节 5每一章的章节名字
    第二步 设置切割文件得到切片文件下标:   5整个目录的文件路径source_path 6第i章 每一章的章节名字capter_name1
    第三步 设置得到第二步的返回值 即:切片下标和对应文件内容的list
    第四步 拆分大文件内容到不同文件里,用来做每一章每个算法题的笔记，可选
    第五步 生成带目录注释的.py文件
        调用makefile()函数来生成文件
        参数列表说明:1路径 2每一章多少小节 3编号+章节名称 4书名 5每一章的章节名字 6第i章 每一章的章节名字capter_name1 7对应文件内容的list
    """
# ——————————————————————————————————————————————————————————————————————————————————————————





# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(now)
# print(type(now))
# cpath = os.getcwd()
# print(cpath)

"""
    创建的第7本书
        程序员代码面试指南：IT 名企算法与数据结构题目最优解 / 左程云著 第二版
        2Deep Learning
    """
    # bookname = "python_180_zuo.pdf(程序员代码面试指南整理)"
    # path = r'../python_arithmetic/'
    # tpath = os.path.realpath(path)  # 绝对路径
    # # print(tpath)
    # lessons_list_large = []
    # capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # capter_name = ['栈和队列', '链表问题', '二叉树问题', '递归和动态规划', '字符串问题', '大数据和空间限制','位运算', '数组和矩阵问题', '其他题目']
    # lessons_list = [11, 20, 24, 20, 25, 7, 6, 31, 37]
    # cl = len(capter_list)
    # # print(cl)
    # cnamedir_list = []
    # for i in range(1, cl + 1):
    #     cname = str(i) + capter_name[i - 1]
    #     # print(cname)
    #     cnamedir_list.append(cname)
    # print(cnamedir_list)

    # 第一步创建文件夹
    # try:
    #     for i in range(1, cl + 1):
    #         cname = path + str(i) + capter_name[i - 1]
    #         # print(path + str(i) + capter_name[i-1])
    #         os.makedirs(path + str(i) + capter_name[i-1])
    # except:
    #     print("@@@@文件夹已创建了")
    # 第二步 测试参数
    # print(tpath, lessons_list, capter_list, now, bookname)
    # print(tpath, lessons_list, cnamedir_list, now, bookname)
    # 第三部 执行makefile
    # makefile(tpath, lessons_list, capter_list, now, bookname)






