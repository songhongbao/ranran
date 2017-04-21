# -*- coding: utf-8 -*-


class display:
    _info = dict()

    def __init__(self, info):
        self._info = info

    @staticmethod
    def show(self):
        print 'done'

    def show_help(self):
        self._info = dict()
        self._info['list'] = 'Show script list'
        self._info['show script'] = 'Instructions of the script (e.g. show sub_domain)'
        self._info['use script'] = 'Use the script (e.g. show sub_domain)'
        self.show()

