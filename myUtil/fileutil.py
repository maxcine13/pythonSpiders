# -*- coding:utf-8 -*-
import os, csv
import pandas as pd


def writefile(filename, mode='w', string=''):
    with open(filename, mode) as f:
        f.write(str(string) + '\n')


def readfile(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')


def readfileString(filename):
    with open(filename, 'r') as f:
        return f.read()


def deletefileline(filename, string):
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f_w:
        for line in lines:
            if str(string) in line:
                continue
            f_w.write(line)


def deleteFile(filename):
    if os.path.exists(filename):
        os.remove(filename)


# 切分中文字符串
def split_cn(string, start, end):
    # 先转换成unicode，再取子串，然后转换成utf-8
    return string.decode('utf-8')[start:end].encode('utf-8')


# 合并文件夹内的文件
def merger(file_dir, resultname):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(files)  # 当前路径下所有非目录子文件
        f = open(root + '/' + resultname, 'w')
        for filename in files:
            filepath = root + '/' + filename
            # 遍历单个文件，读取行数
            for line in open(filepath):
                f.writelines(line)
        f.close()


# 文件去重
def file_dis(filename, result):
    # if not os.path.exists(result):  # 如果目录不存在则创建
    #     os.makedirs(result)
    with open(filename, 'r') as f:
        s = f.readlines()
        ss = list(set(s))
        with open(result, 'a') as ff:
            for i in range(1, len(ss)):
                ff.write(ss[i] + '\n')


# 对文件夹内的所有文件去重
def files_dis(file_dir, out_dir):
    if not os.path.exists(out_dir):  # 如果目录不存在则创建
        os.makedirs(out_dir)
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(files)  # 当前路径下所有非目录子文件
        for f in files:
            file_dis(root + '\\' + f, out_dir + '\\' + f)


# 切分文件
def split_file(file_name, line_count=20000):
    if file_name and os.path.exists(file_name):
        dirs = os.path.dirname(file_name)
        result_dir = dirs + '\\result\\'
        if not os.path.exists(result_dir):  # 如果临时目录不存在则创建
            os.makedirs(result_dir)
        print dirs
        print result_dir
        try:
            with open(file_name) as f:  # 使用with读文件
                temp_count = 0
                temp_content = []
                part_num = 1
                for line in f:
                    if temp_count < line_count:
                        temp_count += 1
                    else:
                        part_file_name = result_dir + "qiye_" + str(part_num) + ".txt"
                        with open(part_file_name, "w") as part_file:
                            part_file.writelines(temp_content[0])
                        part_num += 1
                        temp_count = 1
                        temp_content = []
                    temp_content.append(line)
                else:  # 正常结束循环后将剩余的内容写入新文件中
                    with open(part_file_name, "w") as part_file:
                        part_file.writelines(temp_content[0])
        except IOError as err:
            print(err)
    else:
        print("%s is not a validate file" % file_name)


# 读取xls文件转换成csv文件
def xls2csv(in_dir, out_dir):
    if not os.path.exists(out_dir):  # 如果临时目录不存在则创建
        os.makedirs(out_dir)
    for root, dirs, files in os.walk(in_dir):
        for f in files:
            filename = str(f).split('.')[0]
            input_file = root + '\\' + f
            output_file = out_dir + '\\' + filename + '.csv'
            # print input_file, output_file
            data = pd.read_excel(input_file, 'sheet1', index_col=0)
            data.to_csv(output_file, encoding='utf-8')


# 写入到csv文件
def write2csv(filename, list):
    with open(filename, "a") as csvfile:
        writer = csv.writer(csvfile)
        # #先写入columns_name
        # writer.writerow(["index","a_name","b_name"])
        # 写入多行用writerows
        writer.writerow(list)
