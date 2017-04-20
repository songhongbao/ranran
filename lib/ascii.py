# -*- coding:utf-8 -*-

import random
import platform
import os
import re


def color2ascii(color=None):
    # color end
    if not color:
        return '\033[0m'
    # different color ascii
    color_map = {
        'black': '\033[1;30m',
        'yellow': '\033[1;33m',
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


def info2comment(info, length):
    length -= len(info)
    start = int(length / 2 - 3) * '#'
    end = (length - int(length / 2) - 3) * '#'
    return start + '   ' + info + '   ' + end


def get_ascii(ascii_name, color):
    ascii_art_path = os.path.dirname(os.path.realpath(__file__)) + '/../data/AsciiArt/'
    with open(ascii_art_path + ascii_name, 'r') as content_file:
        content = content_file.read()
    if 'Windows' in platform.system():
        return content
    # different ascii art use different color style
    if ascii_name == 'giraffe':
        content = re.sub(r'(\\)([^\\\n]+)(\\#)', r'\1' + color2ascii('red') + r'\2' + color2ascii() + r'\3', content)
    elif ascii_name == 'butterfly':
        content = re.sub(r'(#+)', color2ascii('green') + r'\1' + color2ascii(), content)
        content = re.sub(r'(=+)', color2ascii('blue') + r'\1' + color2ascii(), content)
    elif ascii_name == 'beetle':
        content = re.sub(r'(m+)', color2ascii('blue') + r'\1' + color2ascii(), content)
    elif ascii_name == 'dog' or ascii_name == 'elephant':
        content = re.sub(r'([a-zA-Z ]+!)', color2ascii('red') + r'\1' + color2ascii(), content)
    elif ascii_name == 'monkey':
        content = re.sub(r'([oO])', color2ascii('yellow') + r'\1' + color2ascii(), content)
    elif ascii_name == 'bear':
        content = re.sub(r'(\.-\.|\(   \)|\'-\'|O)', color2ascii('red') + r'\1' + color2ascii(), content)
        content = re.sub(r'(\*+)', color2ascii('white_red') + r'\1' + color2ascii(), content)
    elif ascii_name == 'dolphin':
        content = re.sub(r'(~{10,})', color2ascii('white_blue') + r'\1' + color2ascii(), content)
    # drawing picture
    rep = {
        '\033': color2ascii() + '\033',
        color2ascii(): color2ascii() + color2ascii(color)
    }
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    content = pattern.sub(lambda m: rep[re.escape(m.group(0))], content)
    content = color2ascii(color) + '\r\n' + content + color2ascii()
    return content


def output():
    arts = [
        ['giraffe', 'yellow', 'Giraffe -- A Lovely Animal!'],
        ['butterfly', 'yellow', 'More than 750 species of butterflies have been recorded.'],
        ['beetle', 'red', 'I\'m not bug! I\'m beetle.'],
        ['python', 'green', 'Oh, Snake! Wow, Python!'],
        ['dog', 'white', ''],
        ['monkey', 'white', 'Programmers and monkeys are good friends.'],
        ['bear', 'white', 'The bear hates the Antarctic.'],
        ['dolphin', 'white', 'Dolphin in the sea song.'],
        ['elephant', 'green', ''],
    ]
    [name, color, desc] = random.choice(arts)
    print get_ascii(name, color)
    print desc + '\r\n'
    chars = '##############################################'
    print chars
    print info2comment('RanRan Framework V1.0', len(chars))
    print info2comment('A simple tools for hack', len(chars))
    print info2comment('email shy[at]ranshy.com', len(chars))
    print info2comment('blog http://love.ranshy.com', len(chars))
    print chars

