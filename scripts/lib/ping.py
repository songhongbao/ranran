# -*- coding:utf-8 -*-
from platform import system as system_name
from os import system as system_call


def ping(host, count=4):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """
    parameters = "-n " + str(count) if system_name().lower() == "windows" else "-c " + str(count)
    status = system_call("ping " + parameters + " " + host)
    if status == 0:
        return True
    else:
        return False
