import rsocket

fs = rsocket.RSocket()
fs.listen()
while True:
    data = fs.receive()
    if not data:
        continue
    print data
fs.close()
