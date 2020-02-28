import socket

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST_CONNECT = "127.0.0.1"
PORT_CONNECT = 6000

endecode_data = "ascii"
buffer_size = 1024

ss.connect((HOST_CONNECT, PORT_CONNECT))

data = input("Me >> ")
ss.send(data.encode(endecode_data))

data = ss.recv(buffer_size)
data = data.decode(endecode_data)
print(data)