# -*- coding: utf-8 -*-
import os


def get_list():
    script_path = os.path.dirname(os.path.realpath(__file__)) + '/../scripts/'
    names = []
    for script in os.listdir(script_path):
        if script[-3:] == '.py':
            names.append(script[0:-3])
    return names
