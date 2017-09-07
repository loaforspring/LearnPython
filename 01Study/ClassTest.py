#!/usr/bin/python3

#导入模块方式一
import LSRequest #使用时需加上模块名

#导入模块方式二
# from LSRequest import *


cifuUrlStr = 'http://172.10.3.75:80/blessing/requestBlessing.do?userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&toUserId=7'
# request = LSRequest("http://www.baidu.com")

# 导入方式一，使用时要加上模块限定
request = LSRequest.LSRequest(cifuUrlStr)
print(request.startRequest())

# 导入方式二，使用时不用模块限定
# request = LSRequest(cifuUrlStr)
# print(request.startRequest())
