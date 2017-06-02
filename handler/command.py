# -*- coding: utf-8 -*-
from config import ranran
import sys
from inspect import getargspec
import script
from lib import log

# RanRan role's name(default ranran), switch name when use script
name = 'ranran'


def _get(key):
    """
    get the script param\'s value
    get ip
    """
    a = 1
    pass


def _help():
    """
    help information
    """
    print 'Options and arguments:'
    for func_name in dir(sys.modules[__name__]):
        if func_name[0] != '_' or func_name[0:2] == '__':
            continue
        func = getattr(sys.modules[__name__], func_name)
        func_require = len(getargspec(func).args)
        func_msg = ''
        func_eg = ''
        if func.__doc__:
            info = func.__doc__.strip().split('\n')
            func_msg = info[0]
            if len(info) >= 2:
                func_eg = info[1]
        print func_name.ljust(10) + ': ' + func_msg.strip()
        if func_require:
            print str(func_require).rjust(13) + ' param required'
        if func_eg:
            print 12 * ' ' + 'eg. ' + func_eg.strip()


def _info():
    """
    show the script param list, some params is set default value
    """
    pass


def _list():
    """
    all script that you can use
    """
    for script_name in script.get_list():
        print script_name


def _set(key, value):
    """
    set a value to the script param.
    set ip 192.168.72.9
    """
    pass


def _status():
    """
    the script running status, percent, threads, etc.
    """
    pass


def _use(script_name):
    """
    use script, switch from one directory to another
    use ping
    """
    if script_name not in script.get_list() or script_name != 'ranran':
        log.error('script ' + script_name + ' is not found, type list to get more info.')
    global name
    name = script_name


def _version():
    """
    show RanRan version
    """
    print 'RanRan version is ' + ranran.version


