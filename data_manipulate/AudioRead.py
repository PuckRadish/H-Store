from pydub import AudioSegment
import wave
import io
import os
import numpy as np
import matplotlib.pyplot as plt   #专业绘图库
from PIL import Image
import pylab
from scipy.io import wavfile
from Storage.DBConnector import *


# 先从本地获取 mp3 的 bytestring 作为数据样本
filepath = "../data_file/" #添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称

def AudioStore(file):
    f = wave.open(file,'rb')
    print(file)
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    strData = f.readframes(nframes)
    wavaData = np.frombuffer(strData,dtype=np.int32)
    waveData = wavaData*1.0/(max(abs(wavaData)))

    Pgconn = pgConnect()
    
    # plot
    time = np.arange(0,nframes)*(1.0/framerate)
    print(wavaData.size)
    print(nframes)
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.title("Single channel wavedata")
    plt.grid('on')#标尺，on：有，off:无。
    plt.plot(time,waveData)


