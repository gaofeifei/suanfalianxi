#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime
import time
def makefile(path,s,d,now,bookname):

    ld = len(d)
    print(ld)
    num = 0
    for root, dirs, files in os.walk(path):
        #print(root)#绝对路径
        # print(dirs)
        for i in dirs:
            sub_path = path+"\\"+i
            if os.path.exists(sub_path):
                # print(sub_path)
                os.chdir(sub_path)#转换路径
                open(i+"catalogue.txt","a+")
                # cpath = os.getcwd()#当前目录
                while 1:
                    # print(num)
                    num += 1
                    if num > 0 and num <= ld:
                        # print(num)
                        for j in range(1,s[num-1]+1):
                            # print(str(d[num-1])+"."+str(j)+".py")
                            filename = str(d[num - 1]) + "." + str(j) + ".py"
                            # print(filename)
                            ccpath= path+"\\"+str(d[num - 1])
                            # print("hahaha:"+ccpath)
                            f = open(ccpath+"\\"+filename, 'w+')#直接打开一个文件，如果文件不存在则创建文件
                            # f.write(str(d[num - 1]) + "." + str(j))
                            wline = '"""\nBOOK:'+bookname+"\n"+str(d[num - 1]) + "." + str(j)+'\n'+'\n"""'+'\n'+"'''"+"author:feifeigao cheer!!!"+"'''"+'\n' + "'''" +now+ "'''"+'\n'+'\n'
                            # print(wline)
                            f.writelines(wline)
                            f.close()
                    else:
                        break

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(now)
    # print(type(now))
    cpath = os.getcwd()
    # print(cpath)

    """第一本书
    1python_cookbook 书的 学习地图 结构
    bookname = "PYTHON_COOKBOOK"
    # path = str(input('the path:'))
    #content = str(input('please write the content into the new file:'))
    #now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(now)
    # print(type(now))
    cpath = os.getcwd()
    # print(cpath)
    lessons_list = [20, 20, 16, 16, 21, 13, 12, 25, 25, 15, 13, 14, 15, 14, 21]  # 目录中对应的每章有多少小节 例如第一章有20小节，每节建一个py文件
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 目录中对应的有多少章,每章建一个文件夹
    path = r'../shujujiegouyusuanfa/1python_cookbook/'
    tpath = os.path.realpath(path)  # 绝对路径
    # print(tpath)
    """

    """第二本书
    python深度学习
    2Deep Learning with Python 书的 学习地图 结构

    bookname = "2Deep Learning with Python"
    path = r'../shujujiegouyusuanfa/3deep_learning_with_python/'
    tpath = os.path.realpath(path)  # 绝对路径
    print(tpath)
    # lessons_list_large = [3, 5, 6, 5, 4, 4, 3, 5, 5]
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lessons_list = [21, 24, 30, 18, 13, 23, 14, 22, 19]
    cl = len(capter_list)
    print(cl)
    """

    """第三本书
    TensorFlow深度学习 龙书
    Deep-Learning-with-TensorFlow-book

    bookname = "book_DeepLearning with TensorFlow"
    path = r'../shujujiegouyusuanfa/2DeepLearning with TensorFlow/'
    tpath = os.path.realpath(path)  # 绝对路径
    print(tpath)
    # lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #龙书每章都除去 参考文献这一节，会比真实的少一节
    lessons_list = [1, 4, 9, 10, 8, 8, 9, 7, 8, 14, 12, 5, 8, 6, 6]
    cl = len(capter_list)
    print(cl)
    """

    """第四本书
    动手学深度学习
    Dive into 2Deep Learning

    bookname = "Dive into 2Deep Learning"
    path = r'../shujujiegouyusuanfa/4book_Dive into 2Deep Learning/'
    tpath = os.path.realpath(path)  # 绝对路径
    print(tpath)
    # lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lessons_list = [4, 15, 72, 16, 39, 32, 26, 17, 48, 36]
    cl = len(capter_list)
    print(cl)
    """

    """
    创建的第5本书
        趣学算法
        Fun learning algorithm
    bookname = "Fun learning algorithm"
    path = r'../shujujiegouyusuanfa/Fun learning algorithm/'
    tpath = os.path.realpath(path)  # 绝对路径
    print(tpath)
    lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7]
    lessons_list = [6, 7, 6, 11, 8, 5, 11]
    cl = len(capter_list)
    # print(cl)
    """
    """
    创建的第6本书
        花书-李宏毅
        2Deep Learning

    bookname = "2Deep Learning"
    path = r'../shujujiegouyusuanfa/2Deep Learning/'
    tpath = os.path.realpath(path)  # 绝对路径
    print(tpath)
    lessons_list_large = []
    capter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    lessons_list = [1, 12, 22, 5, 26, 19, 16, 28, 11, 19, 10, 17, 5, 12, 6, 13, 7, 8, 9, 32]
    cl = len(capter_list)
    # print(cl)
    """


    # 第一步创建文件夹
    # try:
    #     for i in range(1, cl + 1):
    #         os.makedirs(path + str(i))
    # except:
    #     print("@@@@文件夹已创建了")
    # 第二步 测试参数
    # print(tpath, lessons_list, capter_list, now, bookname)
    # 第三部 执行makefile
    # makefile(tpath, lessons_list, capter_list, now, bookname)



# os.path 模块中的函数来操作路径名
#path = r'../1python_cookbook/'
#os.path.exists(path)#判断路径是否存在
# print(os.path.exists(path))
#tpath = os.path.realpath(path)#绝对路径
#print(tpath)
#创建文件夹
# for i in range(1,16):
#     os.makedirs(path+str(i))
# 在文件夹新建文件
# 以 文件夹.数字.py
#返回文件路径
#dirname = os.path.dirname(path)
# print(os.chdir(dirname+str(i)))
#print(os.listdir(tpath))
#for i in range(1,16):
#print(os.chdir(tpath+"\\"+str(i)))

