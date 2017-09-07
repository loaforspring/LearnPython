#!/usr/bin/python3

#引用一个网络库
import urllib.request

class LSRequest(object):
    """
    object表示LSRequest继承自object类    
    对一个指定的url发起一个get请求,返回响应结果，可以抓取一个网页内容
    """
    def __init__(self, url):
        self.requestUrl = url#会自动创建一个全局变量
        self.__privateParm = 'private'#私有变量，不允许外部访问
        print('init with ' + url)
        pass

    def startRequest(self):
        #
        print('start request with ' + self.requestUrl)
        # if requestUrl:
        # 发起一个网络请求
        resp = urllib.request.urlopen(self.requestUrl)
        response = resp.read() #当该语句读取的返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中
        responseStr = bytes.decode(response)
        # print(responseStr)
        return responseStr


# cifuUrlStr = 'http://172.10.3.75:80/blessing/requestBlessing.do?userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&toUserId=7'
# request = LSRequest(cifuUrlStr)
# print(request.startRequest())

cifuUrlStr = 'http://www.baidu.com'
request = LSRequest(cifuUrlStr)
print(request.startRequest())


print("Test branch")