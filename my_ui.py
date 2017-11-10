#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : my_ui.py
# @Author: Hui
# @Date  : 2017/10/26
# @Desc  :

from tkinter import*
from PIL import Image, ImageTk

'''
#TestFrame用于验证码抓取后的GUI显示，为了方便查看机器预测的
#值是否正确
'''

class TestFrame(Frame):
    def __init__(self, master, height=80, width=100, nums=6):
        super().__init__(master)
        self.height = height
        self.width = width
        self.nums = nums    #单次显图片的数量
        self.labels = []    #图片的标签
        self.entrys = []    #预测值的文本框
        self.currentPage = 0 #当前页
        self.images = []    #图片
        self.values = []    #预测值

        for i in range(self.nums):
            label = Label(self, width= self.width, height=self.height, relief=RIDGE)
            label.grid(row=i, column=0)
            self.labels.append(label)
            entry = Entry(self, relief=SUNKEN, textvariable=StringVar(self, 'preidct'),
                          font='Helvetica 20 bold')
            entry.grid(row=i, column=1)
            self.entrys.append(entry)
        self.pack()

    #初始化传入值
    def addPicture(self, images, value):
        self.images = images
        self.values = value

    #事件翻页
    def nextPage(self, e):
        #pages = len(file)/self.nums
        file = self.images[self.currentPage * self.nums: (self.currentPage + 1) * self.nums]
        value = self.values[self.currentPage * self.nums: (self.currentPage + 1) * self.nums]
        for i in range(self.nums):
            img = Image.open(file[i]).resize((self.height-10, self.width-10))
            img = ImageTk.PhotoImage(img)
            self.labels[i].configure(image=img)
            self.labels[i].image = img
            #self.entrys[i]['text'] = value[i]
            self.entrys[i].config(textvariable=StringVar(self, value[i]))

        #下一页
        self.currentPage += 1
