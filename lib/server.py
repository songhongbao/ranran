import rsocket

fs = rsocket.RSocket()
fs.listen()
while True:
    data = fs.receive()
    if not data:
        continue
    fs.send('aa')
    fs.close()
    exit(0)
