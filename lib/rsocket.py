# -*- coding: utf-8 -*-
import socket
import sys


class RSocket:
    _address = ('127.0.0.1', 7729)
    _socket = None

    def __init__(self):
        sys.path.append("..")
        # import config
        # if config.port:
        #   self._address = ('127.0.0.1', config.port)

    def listen(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # fix socket.error: Address already in use
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(self._address)
        self._socket.listen(10)
        self._socket.settimeout(60)

    def client(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(self._address)

    def receive(self):
        try:
            result = self._socket.recv(1024)
        except socket.timeout:
            result = None
        except Exception, e:
            print e
            result = False
        finally:
            return result

    def send(self, msg):
        if msg == '':
            return True
        try:
            self._socket.send(msg)
            result = True
        except Exception, e:
            print e
            result = False
        finally:
            return result

    def close(self):
        self._socket.close()
        self._socket = None
