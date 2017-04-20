import rsocket

fs = rsocket.RSocket()
fs.client()
fs.send('111')
