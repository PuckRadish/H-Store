import os
import scipy
from scipy.io import wavfile
from AudioRead import AudioStore

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
          if  os.path.splitext(file)[-1] in ['.wav',]:
               AudioStore(file)
          elif os.path.splitext(file) in ['.mp4',]:

          elif os.path.splitext(file) in ['.mp4',]:

          else:

