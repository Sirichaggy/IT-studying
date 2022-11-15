import socket

sock = socket.socket()
sock.bind(('localhost', 8888))
sock.listen(10)

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
    print(data.decode())

conn.close()