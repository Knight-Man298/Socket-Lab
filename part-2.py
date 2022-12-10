import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_number = 298

s.connect(('localhost', port_number))

message = s.recv(1024)

print(message.decode("utf-8"))