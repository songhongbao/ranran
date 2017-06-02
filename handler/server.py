# -*- coding: utf-8 -*-
from lib import ascii
from lib import log
from handler import command
from inspect import getargspec
from lib.color import color2ascii


def stop():
    print 'See you!'
    # todo
    exit(0)


def start():
    # ascii.output()
    log.info('Starting RanRan Framework', save=True)
    while True:
        try:
            name = color2ascii('yellow_') + command.name + color2ascii()
            user_command = raw_input(name + '$ ')
            if not user_command:
                continue
            elif user_command == 'exit' or user_command == 'quit':
                stop()
            # command init
            args = [x for x in user_command.split(' ') if x]
            if '_' + args[0] in dir(command):
                func = getattr(command, '_' + args[0])
                param_require = len(getargspec(func).args)
                param = args[1:]
                if param_require != len(param):
                    log.error(args[0] + ' requires ' + str(param_require) + ' param(s), ' + str(len(param)) + ' give')
                    continue
                func(*param)
            else:
                log.error('command ' + args[0] + ' is invalid. Please input help to get info.')
        except KeyboardInterrupt:
            print '\r\nPlease input exit/quit to exit.'
            continue
