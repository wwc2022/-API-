from tkinter import *

from urllib import request
from urllib import parse

import json
import hashlib  


if __name__ == "__main__":
    
    root = Tk()
    root.title("单词翻译器")
    root['width'] = 300;root['height'] = 130
    
    Label(root,text='输入想要翻译的内容：',width=18).place(x=1,y=1)
    Entry1 = Entry(root,width=20)
    Entry1.place(x=120,y=1)
    
    Label(root,text='翻译的结果：',width=18).place(x=1,y=20)
    s = StringVar()
    s.set("大家好，这是测试")
    Entry2 = Entry(root,width=20,textvariable=s)
    Entry2.place(x=120,y=20)
    
    Button1 = Button(root,text='翻译',width = 8)
    Button1.place(x=70,y=80)
    Button2 = Button(root,text='清空',width = 8)
    Button2.place(x=180,y=80)
    #给Button绑定鼠标监听事件
   # Button1.bind("<Button-1>",leftClick)
   # Button2.bind("<Button-1>",leftClick2)
    root.mainloop()
    
    
    
    