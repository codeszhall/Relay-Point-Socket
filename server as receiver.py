import socket

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST = ""
PORT = 8080
ss.bind((HOST, PORT))

elgib_host = 1000
ss.listen(elgib_host)

buffer_size = 1024

endecode_data = "ascii"
status_success_response = "200 OK"

while True :
    conn, addr = ss.accept()
    client_addr = addr[0]
    message = conn.recv(buffer_size)
    message = message.decode(endecode_data)
    print("Status:", status_success_response, " From:", client_addr, " Message:", message[9:])
    conn.close()

