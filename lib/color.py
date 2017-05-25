# -*- coding:utf-8 -*-
import platform


# windows platform output without colors
def color2ascii(color=None):
    if 'Windows' in platform.system():
        return ''
    # color end
    if not color:
        return '\033[0m'
    # different color ascii
    color_map = {
        'black': '\033[1;30m',
        'yellow': '\033[1;33m',
        'yellow_': '\033[33m',
        'red': '\033[1;31m',
        'blue': '\033[1;34m',
        'green': '\033[1;32m',
        'purple': '\033[1;35m',
        'white': '\033[1;37m',
        'white_red': '\033[1;37;41m',
        'black_white': '\033[1;30;47m',
        'white_blue': '\033[1;37;44m',
    }
    return color_map[color]
