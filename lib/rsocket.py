# -*- coding: utf-8 -*-
import socket
from config import ranran
from lib import log


class RSocket:
    _address = ('127.0.0.1', 7729)
    _socket = None

    def __init__(self):
        if hasattr(ranran, 'port'):
            self._address = ('127.0.0.1', ranran.port)

    def listen(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # fix socket.error: Address already in use
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(self._address)
        self._socket.listen(5)
        self._socket.settimeout(5)

    def receive(self):
        try:
            conn = self._socket.accept()[0]
            result = conn.recv(1024)
        except socket.timeout:
            print 'time out'
            return None
        except Exception, e:
            log.error(e, display=False, save=True)
            return False
        finally:
            return result

    def send(self, msg):
        if msg == '':
            return True
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.connect(self._address)
            self._socket.send(msg)
            return True
        except Exception, e:
            log.error(e, display=False, save=True)
            return False

    def close(self):
        self._socket.close()
        self._socket = None
