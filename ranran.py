# -*- coding:utf-8 -*-
from lib import ascii

# ascii.output()





from lib.rsocket import RSocket

fs = RSocket()
fs.listen()
fs.send('111')
exit(0)
fs = RSocket()
fs.listen()
while True:
    data = fs.receive()
    if not data:
        continue
    print data
fs.close()




