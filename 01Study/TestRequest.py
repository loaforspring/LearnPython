# 
import urllib.request
import time

# userIds = ['5', '7']

# for userId in userIds:
#     # url = 'http://172.10.3.75:80/blessing/requestBlessing.do?userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&toUserId='+userId
#     # url = 'http://pmir.3g.qq.com?)m 9ԥ5'
#     url = 'http://172.10.3.75:80/imredpacket/sendRedPacket.do?msg=%E6%81%AD%E5%96%9C%E5%8F%91%E8%B4%A2%EF%BC%8C%E5%A4%A7%E5%90%89%E5%A4%A7%E5%88%A9&userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&money=1.00&sourceType=2&isPrivate=1&toUserId=7'
#     print(url)
 
    # i = 0
    # while i < 100:
#         resp=urllib.request.urlopen(url)
#         print(resp)
#         html=resp.read()
#         print(html)
#         i = i+1
#         time.sleep(0.2)

# http://172.10.3.75:80/blessing/requestBlessing.do?userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&toUserId=5



# url = 'http://172.10.3.75:80/imredpacket/sendRedPacket.do?msg=%E6%81%AD%E5%96%9C%E5%8F%91%E8%B4%A2%EF%BC%8C%E5%A4%A7%E5%90%89%E5%A4%A7%E5%88%A9&userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&money=0.00&sourceType=2&isPrivate=1&toUserId=7'

def sendGetRequest(urlStr):
    print('Read send get request with url' + urlStr)
    resp = urllib.request.urlopen(urlStr)
    response = resp.read() #当该语句读取的返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中
    print(bytes.decode(response))


def draw(): 
    print('道具抽奖')
    drawUrl = 'http://172.10.3.75:80/turntablePrize/doPropDraw.do?deviceType=1&phoneModel=MX4+Pro&userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&systemVersionRelease=5.1.1&imei=867324020493496&deviceCode=D83F91C9106E37D6&systemVersion=22&deviceId=CCC87CBF4881C9F7&luckDrawNum=1&androidId=221deab09d1c2b1f'
    sendGetRequest(drawUrl)

# draw()

def requestCifu(userIdStr):
    print('请求赐福：'+userIdStr)
    cifuUrlStr = 'http://172.10.3.75:80/blessing/requestBlessing.do?userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&toUserId=' + userIdStr
    sendGetRequest(cifuUrlStr)

# 5是姚留洋
# 7是王全启
# requestCifu('7')

def sendMoney(money, userId):
    sendMoneyUrl = 'http://172.10.3.75:80/imredpacket/sendRedPacket.do?msg=%E6%81%AD%E5%96%9C%E5%8F%91%E8%B4%A2%EF%BC%8C%E5%A4%A7%E5%90%89%E5%A4%A7%E5%88%A9&userCertificate=A8AC2E3437C415EF2AC6D60BD3E3A6E3&money=' + money + '&sourceType=2&isPrivate=1&toUserId=' + userId
    print(sendMoneyUrl)
    sendGetRequest(sendMoneyUrl)

# sendMoney('0.01', '5')

# i = 0
# while i < 100:
    # sendMoney('0.01', '5')
    # sendMoney('0.01', '7')
    # i = i + 1
