import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 9001))

conn, addr = s.accept()

while True:
  command = input("CMD> ")

  if command == 'exit':
    conn.send("exit".encode())
    conn.close()
    break
  else:
    conn.send(command.encode())
    print(conn.recv(1024).decode())
