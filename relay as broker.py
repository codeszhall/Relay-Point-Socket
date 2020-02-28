import socket

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST_BIND = ""
PORT_BIND = 6000
HOST_CONNECT = "127.0.0.1"
PORT_CONNECT = 8080
ss.bind((HOST_BIND, PORT_BIND))

elgib_host = 1000
ss.listen(elgib_host)

buffer_size = 1024

endecode_data = "ascii"
counter = 0

while 1 :
    ss_new = s.socket(IPv4, TCP)
    conn, addr = ss.accept()
    client_addr = addr[0]
    message = conn.recv(100)
    conn.close()
    message = message.decode(endecode_data)
    message = client_addr + message
    message = message.encode(endecode_data)
    ss_new.connect((HOST_CONNECT, PORT_CONNECT))
    ss_new.send(message)
    counter+=1
    print("[" + str(counter) + "]", "Message from: ", client_addr, " has successfully been sent to server")