# -*- coding: utf-8 -*-
from config import ranran


description = {
    'get': {
        'msg': 'get the script param\'s value',
        'example': 'get',
        'require': 1
    },
    'help': {
        'msg': 'help information'
    },
    'info': {
        'msg': 'show the script param list, some params is set default value'
    },
    'list': {
        'msg': 'all script that you can use'
    },
    'set': {
        'msg': 'set a value to the script param',
        'example': 'set ip 192.168.72.9',
        'require': 2
    },
    'status': {
        'msg': 'the script running status, percent, threads, etc.'
    },
    'use': {
        'msg': 'use script, switch from one directory to another',
        'example': 'use ping',
        'require': 1
    },
    'version': {
        'msg': 'show RanRan version'
    }
}

# RanRan role's info, on
role = {
    # command role name, only output
    'name': 'ranran',
    # command script
    'script': ''
}

scripts = [
    'ping',
    'sub-domains'
]


def _get():
    pass


def _help():
    print 'Options and arguments:'
    for opt in sorted(description.iterkeys()):
        value = description[opt]
        print opt.ljust(10) + ': ' + value['msg']
        if 'require' in value:
            print str(value['require']).rjust(13) + ' param required'
        if 'example' in value:
            print 12 * ' ' + 'eg. ' + value['example']


def _info():
    pass


def _list():
    print script.get_list()
    pass


def _set():
    pass


def _status():
    pass


def _use(script, typess=1):
    print script


def _version():
    print 'RanRan version is ' + ranran.version




