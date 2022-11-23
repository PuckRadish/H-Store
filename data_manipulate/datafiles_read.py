import os

'''
    Read all files in the user-defined file directory!
'''

File_directory = ''
files= os.listdir(File_directory)

KV_file = []
relational_file = []
TS_file = []
Web_file = []

for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          if  os.path.splitext(file)[-1] in ['.a',]:

          elif
          f = open(File_directory +"/"+file); #打开文件
          iter_f = iter(f); #创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              str = str + line
          s.append(str) #每个文件的文本存到list中
print(s) #打印结果
