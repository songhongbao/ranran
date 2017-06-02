# -*- coding: utf-8 -*-
import os


def get_list():
    script_path = os.path.dirname(os.path.realpath(__file__)) + '/../scripts/'
    names = []
    for script in os.listdir(script_path):
        if os.path.isdir(script_path + '/' + script) and os.path.isfile(script_path + '/' + script + '/' + 'readme'):
            names.append(script)
    return names

