computer networking -- from up to down
------------------------------------------
但是有一个问题，我一直没办法在别的主机上通过ip地址访问我的服务器，一开始在自己的电脑上也没有登陆成功，但是第二天挂了个vpn之后自己的电脑就能连上了，
，但是用其他主机还是不ok，我猜测可能和win10网络设置有关系···之后再仔细学一下这一块的内容，毕竟我的初衷是熟悉python而不是网络编程...然后还有一个问题，就是每一次只能成功连接一次，但是第二次就会出现出现这个问题
<br>

然后有时又会出现主机拒绝访问的问题,没有理解这边为啥会出现溢出···有几次第一次是能够成功的

### 第一遍跟着敲的代码

```python
  #import socketserver module
  from socket import *
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a sever socket
  serverPort = 6788

  serverSocket.bind(('',serverPort))
  serverSocket.listen(1)

  while True:
      #Establish the connection
      print('Ready to serve...')
      connectionSocket, addr = serverSocket.accept()
      try:
          message = connectionSocket.recv(2048)
          #获取由客户发送的行
          print('try')
          filename = message.split()[1]
          f = open(filename[1:])
          outputdata = f.read()
          capitalizedSentence = outputdata.upper()
          #转化为大写
      #Send one HTTP header line into socket
          header = ' HTTP/1.1 200 OK\nConnection: open\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
          connectionSocket.send(header.encode())
          #因为只需要回应请求，所以不需要直到用户的IP地址，与UDP连接方式不相同
      #Send the content of the requested file to the client
          for i in range(0, len(outputdata)):
              connectionSocket.send(outputdata[i].encode())
          connectionSocket.close()
      except IOError:
      #Send response message for file not found
          header = ' HTTP/1.1 404 Found'
          connectionSocket.send(header.encode())
          #Close client socket
          connectionSocket.close()

  serverSocket.close()
```
第一次出现的溢出问题
```
Ready to serve...
Traceback (most recent call last):
  File "C:/Users/lenovo/Desktop/webserver.py", line 18, in <module>
try
    filename = message.split()[1]
IndexError: list index out of range
```
### 第二次更新

啊啊啊，通过Google好像把字符溢出问题给解决了，下面是更新过的代码
```python
  #import socketserver module
  from socket import *

  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a sever socket
  serverPort = 6787
  #serverSocket.close()
  serverSocket.bind(('',serverPort))
  serverSocket.listen(1)
  flag=0
  while True:
      #Establish the connection
      print('Ready to serve...')
      connectionSocket, addr = serverSocket.accept()
      flag+=1
      print(flag)
      try:
          message = connectionSocket.recv(1024)
          print(message)
          #获取由客户发送的行
          if not message:
              print('not message')
              connectionSocket.close()
              continue
          filename = message.split()[1]
          print(filename)
          f = open(filename[1:])
          outputdata = f.read()
          capitalizedSentence = outputdata.upper()
          #转化为大写
      #Send one HTTP header line into socket
          header = ' HTTP/1.1 200 OK\nConnection: open\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
          connectionSocket.send(header.encode())
          #因为只需要回应请求，所以不需要直到用户的IP地址，与UDP连接方式不相同
      #Send the content of the requested file to the client
          for i in range(0, len(outputdata)):
              connectionSocket.send(outputdata[i].encode())
          connectionSocket.close()
      except IOError:
      #Send response message for file not found
          print('error')
          header = ' HTTP/1.1 404 Found'
          connectionSocket.send(header.encode())
          #Close client socket
          connectionSocket.close()
  serverSocket.close()
 ```
 主要修改的是这里
 首先要处理message接收到的url为空的情况，这样一来如果没有输入任何数据就不会出现'IndexError: list index out of range'这样子的问题啦
 ```python
 message = connectionSocket.recv(1024)
          print(message)
          #获取由客户发送的行
          if not message:
              print('not message')
              connectionSocket.close()
              continue
 ```
 然后我把输出也贴上来
 ```
   D:\Anaconda3\python.exe C:/Users/lenovo/Desktop/webserver.py
  Ready to serve...
  1
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  2
  b''
  not message
  Ready to serve...
  3
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  4
  b''
  not message
  Ready to serve...
  5
  b'GET /sockt.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/sockt.html'
  error
  Ready to serve...
  6
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nPurpose: prefetch\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  7
  b''
  not message
  Ready to serve...
  8
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  9
  b'GET /sockt.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/sockt.html'
  error
  Ready to serve...
  10
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nPurpose: prefetch\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  11
  b''
  not message
  Ready to serve...
  12
  b'GET /socket.html HTTP/1.1\r\nHost: 10.27.210.166:6787\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: zh-CN,zh;q=0.9,en;q=0.8\r\n\r\n'
  b'/socket.html'
  Ready to serve...
  13
  b''
  not message
  Ready to serve...
 ```
 ### 第三次更新终于找到问题在哪儿了
 
 可以看出来每次的请求连接第一次用‘connectionSocket.recv(1024)’函数都是请求失败的，所以如果是正确输入每次都要连续输入两次，每次要循环两回才能成功读到，暂时还不知道为啥···也就是说在读到过正确的message之后的一次总是会经历读取失败<br>
 半小时后更新！！！啊啊啊我知道问题出在哪里了！<br>
 因为我连接的时候会把全选上整条url,所以实际上发送的是回车而不是输入的地址<br>
 好了<br>
 舒服了<br>
 哈哈哈哈哈哈哈哈哈哈哈<br>
 
 还有加注释老是出不来的问题也解决啦！是因为小圆点用中文输入法打了
 -------------------------------------------------
