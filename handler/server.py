# -*- coding: utf-8 -*-
from lib import ascii
from lib import log
from config import command, ranran
from handler import script


def _parse(user_command):
    args = [x for x in user_command.split(' ') if x]
    # param error
    if args[0] not in command.info:
        log.error('invalid command')
        return False
    info = command.info[args[0]]
    if 'require' not in info:
        info['require'] = 0
    if len(args) != info['require'] + 1:
        log.error(args[0] + ' option requires ' + str(info['require']) + ' param, ' + str(len(args) - 1) + ' give')
        return False
    # init param
    result = dict()
    result['opt'] = args[0]
    if len(args) == 2:
        result['value'] = args[1]
    elif len(args) > 2:
        result['value'] = args[1:]
    return result


def _use(script):
    print script


def _help():
    print 'Options and arguments:'
    for opt in sorted(command.info.iterkeys()):
        value = command.info[opt]
        print opt.ljust(10) + ': ' + value['msg']
        if 'require' in value:
            print str(value['require']).rjust(13) + ' param required'
        if 'example' in value:
            print 12 * ' ' + 'eg. ' + value['example']


def _version():
    print 'RanRan version is ' + ranran.version


def _show():
    print script.get_list()
    pass


def start():
    ascii.output()
    log.info('Starting RanRan Framework', save=True)
    while True:
        try:
            user_command = raw_input(command.role['name'] + '$ ')
            if not user_command:
                continue
            elif user_command == 'exit':
                print 'See you!'
                exit(0)
            param = _parse(user_command)
            if not param:
                continue
            if '_' + param['opt'] in globals():
                if 'value' in param:
                    globals()['_' + param['opt']](param['value'])
                else:
                    globals()['_' + param['opt']]()
            else:
                print 'function todo'
        except KeyboardInterrupt:
            print '\r\nPlease input exit to exit.'
            continue

print __doc__