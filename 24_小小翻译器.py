#-*- coding:UTF-8 -*-
from tkinter import *
from urllib import request
from urllib import parse
import random
import json
import hashlib
 
salt = random.randint(32768, 65536) 

def translate_word(en_str):
    try:  
   
        #simulation browse load host url,get cookie
        URL = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        
        #en_str = input("请输入要翻译的内容：")
        #创建From_Date字典，存储向服务器发送的data
        #Form_Data = {'from':'en','to':'zh','q':en_str,"appid":"20240802002114501",'salt':salt}
        
        Form_Date = {}
        Form_Date['from'] = 'auto'
        Form_Date['to']   = 'zh'
        Form_Date['q']    = en_str
        Form_Date['appid']= '20240802002114501'
        Form_Date['salt'] = str(salt)
        key = 'OgsC8p7QDakpl76bTaGQ'
        
        m = Form_Date['appid']+en_str+Form_Date['salt']+key
        m_md5 = hashlib.md5(m.encode('utf-8'))
        Form_Date['sign'] = m_md5.hexdigest()#hexdigest()方法则是用来获取该MD5对象的十六进制表示的字符串。
        
        data = parse.urlencode(Form_Date).encode('utf-8')  #使用urlencode（）方法转换标准格式
        
        response = request.urlopen(URL,data) #传递Request对象和转换完格式的数据
        print(f"response:{response}")
        
        html = response.read().decode('utf-8') #读取信息并解码
        print(f"html:{html}")
        
        #使用 Python 的 json.load() 和 json.loads() 方法从文件和字符串中读取 JSON 数据。
        # 使用 json.load() 和 json.loads() 方法，
        # 您可以将 JSON 格式的数据转换为 Python 类型，这个过程称为 JSON 解析。
        
        #要从 URL 或文件解析 JSON，请使用 json.load()。要解析包含 JSON 内容的字符串，请使用 json.loads()
        #json.load() 用于从文件中读取 JSON 文档，
        # json.loads() 用于将 JSON 字符串文档转换为 Python 字典。
        translate_results = json.loads(html) #使用JSON

        print(f"translate_results:{translate_results}") 
        
        translate_resluts = translate_results['trans_result'][0]['dst'] #找到翻译结果
        print("翻译的结果是：%s"%translate_resluts)#打印翻译的信息
        return translate_resluts

    except json.JSONDecodeError:  
        print("解析JSON时出错，请检查返回的数据是否为有效的JSON格式。")  
    except Exception as e:  
        print(f"发生了一个错误：{e}")


def leftClick(event):   #"翻译"按钮事件函数
    en_str = Entry1.get()
    print(en_str)
    vText = translate_word(en_str)
    print(vText)
    Entry2.delete(0,END) #修改翻译结果框文字
    Entry2.insert(0,vText)
    
    
def leftClick2(event): #"清空"按钮事件函数
    s.set(" ")
    Entry2.insert(0," ")




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
    Button1.bind("<Button-1>",leftClick)
    Button2.bind("<Button-1>",leftClick2)
    root.mainloop()
    
    
    
    