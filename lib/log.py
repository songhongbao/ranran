# -*- coding: utf-8 -*-
import socket
import os
import config


def log(file_path, content):
    if not os.path.exists(file_path):
        file_path = os.path.dirname(os.path.realpath(__file__)) + '/../log/' + file_path
    print file_path
    print content
    return


def error(content):
    log()


def info(content):
    log(config.info_log, content)

