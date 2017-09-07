import urllib.request
str0 =r' <a title="" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eo83.html">《论电影的七个元素》——关于我对电…</a>'
title0=str0.find(r'<a title')
print(title0)
href0=str0.find(r'href')
print(href0)
html0=str0.find(r'html')
print(html0)
url=str0[href0+6:html0+4]
print(url)
content = urllib.request.urlopen(url).read()#当该语句读取的返回值是bytes类型时，要将其转换成utf-8才能正常显示在python程序中

print(type(content))#此时为bytes类型
print(content.decode('utf-8'))#需要进行类型转换才能正常显示在python中
print(type(content.decode('utf-8')))#返回解码后的类型，此时为str类型
filename= url[-20:]
open(filename,'wb').write(content)#在写文件时，要写成bytes类型的文件‘wb’