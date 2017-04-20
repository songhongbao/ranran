# -*- coding: utf-8 -*-
import os
import traceback
import time
import config


def log(file_path, content):
    if '/' not in file_path:
        file_path = os.path.dirname(os.path.realpath(__file__)) + '/../log/' + file_path
    with open(file_path, "a") as fp:
        fp.write(content)
    return


def error(msg):
    current_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time() + time.timezone + 28800))
    trace_stack = traceback.format_stack()
    content = '----------------------------\n'
    content += 'Time: ' + current_time + '\n'
    content += 'ERROR: ' + str(msg) + '\n'
    content += 'Position: ' + trace_stack[-2]
    content += '----------------------------\n\n'
    log(config.error_log, content)


def info(msg):
    current_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time() + time.timezone + 28800))
    content = '----------------------------\n'
    content += 'Time: ' + current_time + '\n'
    content += 'Action: ' + str(msg) + '\n'
    content += '----------------------------\n\n'
    log(config.info_log, content)

