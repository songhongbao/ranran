#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from config import ranran
from handler import server
from lib import log

reload(sys)
sys.setdefaultencoding('utf8')


def command():
    user_command = raw_input('ranran: ')
    print user_command


def main():
    if len(sys.argv) == 2 and sys.argv[1].startswith(ranran.prefix):
        log.info('Starting RanRan Script + ', save=True)
        # todo add script
        exit(0)
    server.start()

if __name__ == '__main__':
    main()




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




