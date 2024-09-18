from urllib import request
  
if __name__ == "__main__":   
    response = request.urlopen("https://yiyan.baidu.com")  
        
    html = response.read()  
    html = html.decode("utf-8")  
    #print(html)  # 这将打印出HTML内容，但可能非常长，视情况而定 
        
         
    print("*******************************************************")       
    print("geturl打印信息:%s"%(response.geturl()))  # 打印响应头信息，转换为字符串以便与其他字符串相加  
    print("*******************************************************")      
    print("info打印信息：%s:"%(response.info()))  
    print("*******************************************************")  
    print("getcode打印信息:%s"%(response.getcode()))  # 直接打印URL  
    print("*******************************************************")  
 
  
    # 使用 urllib.request.urlretrieve 下载文件  
    #request.urlretrieve("https://exp-picture.cdn.bcebos.com/025d87c0affce186d12a9ec61f1fbee434daeb59.jpg?x-bce-process=image%2Fformat%2Cf_auto%2Fquality%2Cq_80", "aaa.jpg")

    #获取http响应的头信息：
    f = request.urlopen("http://fanyi.baidu.com")
    data = f.read()
    print('status:',f.status,f.reason)
    
    for k,v in f.getheaders():
        print('%s : %s '%(k,v))
        
        
    #使用User Agent隐藏身份
    url = "http://www.csdn.net/"
   
    #写入User Agent信息 
    
    #方法一：
    #4rj]head = {}
    #head['User Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    #rep = request.Resquest(url,headers = head)
    #response = request.urlopen(rep)
    
    #方法二：
    rep = request.Request(url)
    rep.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36')
    
    response = request.urlopen(rep)
    html = response.read().decode('utf-8')
    print(html)