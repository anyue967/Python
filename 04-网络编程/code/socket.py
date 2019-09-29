import socket
import threading	# 线程
import logging
import datetime

'''
Server 
	创建 Socket 对象
	绑定IP地址和Port，bind()方法
	监听，listen()方法
Client
	socket.accept() -> (socket object, address info)
	accept方法阻塞等待客户端建立连接，返回一个新的Socket对象的客户端地址的二元组
	地址是远程客户端地址，IPv4中是一个二元组(clentaddr, port)
		接收数据：recv(buffer[, flags]) 使用缓冲区接受数据
		发送数据：send(bytes)发送数据
socket.recv(bufsize[,flags])	
'''
FORMAT = "%(asctime)s %(threadName) s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

# TCP Server
# https://www.cnblogs.com/chownjy/p/8663024.html
# self指的是类实例对象本身(注意：不是类本身)
class ChatServer:
	def __init__(self, ip='127.0.0.1', port=9999):
		self.addr = (ip, port)			# 属性
		self.sock = socket.socket()
		self.clients = {}

	def start(self):
		self.sock.bind(self.addr)
		self.sock.listen()	# 服务启动

		threading.Thread(target=self.accept, name='accept').start()

	def accept(self):
		while not self.event.is_set():
			s, raddr = self.sock.accept() # 解构
			# 阻塞，返回laddr，raddr=('192.168.10.10', 48678)
			logging.info(raddr)
			logging.info(s)
			self.clients[raddr] = s	# 
			threading.Thread(target=self.recv, name='recv', args=(s, )).start()

	def recv(self, sock:socket.socket):
		while not self.event.is_set():
			try:
				data = sock.recv(1024) # 阻塞，bytes
				logging.info(data)
			except Exception as e:
				logging.error(e)
				data = b'quit'
			if data == b'quit':
				self.clients.pop(sock.getpeername())
				sock.close()
				break

			msg = "ack{} .{} {}".format(
				sock.getpeername(),
				datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S"), 
				data.decode()).encode()
			for s in self.clients.values():
				s.send(msg)

	def stop(self):
		for s in self.clients.values():
			s.close()
		self.sock.close()
		self.event.set()

cs = ChatServer()
cs.start()

while True:
	cmd = input(">>>")
	if cmd.strip() == 'quit':
		cs.stop()
		threading.Event.wait(3)
		break
	logging.info(threading.enumerate())








