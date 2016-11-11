#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
 
# 重命名文件rename.txt到rename1.txt。
#os.rename( "rename.txt", "rename1.txt" )

# 删除一个已经存在的文件rename.txt
#os.remove("rename1.txt")

# 创建目录test
#os.mkdir("test")


# 将当前目录改为"/home/myfile"
#os.chdir("/home/myfile")

# 给出当前的目录
print os.getcwd()

# 删除”/tmp/test”目录
#os.rmdir( "./test"  )