import socket
port_number = 298
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostbyname('localhost'))
s.bind((address,port_number))
s.listen(5)

print("[+] Server listening...")

while True:
 conn,address=s.accept()
 print(f"connection to {address[0]} on {address[1]}")
 conn.send(bytes("Socket Programming in Python", "utf-8"))