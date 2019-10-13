import socket

def send_msg(udp_socket):
	# 发送
	dest_ip = input("请输入对方IP")
	dest_port = int(input("请输入对方PORT"))
	send_data = input("请输入发送的信息")
	udp_socket.snedto(send_data.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(udp_socket):
	# 接收
	recv_data = udp_socket.recvfrom(1024)
	print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))

def main():
	# 创建socket对象
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定信息
	udp_socket = socket.bind("", 7788)

	while True:
		# 发送
		send_msg(udp_socket)

		# 接收
		recv_msg(udp_socket)

if __name__ == "__main__":
	main()