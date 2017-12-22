# coding=utf8

import sys,os
from cfg import *

# casefile = sys.argv[1]
casefile = rootPath + 'tclist.txt'
if not os.path.exists(casefile):
    print(u'用例列表文件不存在')

# 先产生参数文件
with open(casefile,'r') as inf, open('args.txt','w') as outf:

    # 产生用例列表
    arglines = []
    icontent = inf.read().replace('\n','')
    cases = icontent.split('|')
    for case in cases:
        case = case.strip()
        if case:
            arglines.append('--test *' + case)

    # 去除重复部分,可以网上搜索关键字
    arglines = list(set(arglines))

    # 生成用例列表参数行
    argsStr = '\n'.join(arglines)

    # 加上其他参数
    argsStr += '\n--pythonpath ' + rootPath
    argsStr += '\n' + rootPath + 'tc'
    print argsStr

    outf.write(argsStr)

# 再执行自动化测试

os.system('robot -A  args.txt')