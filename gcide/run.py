# This file is placed in the Public Domain.


"runtime"


import time


from .cfg import Config
from .evt import Event


starttime = time.time()


Cfg = Config()


def docmd(clt, txt):
    cmd = Event()
    cmd.channel = ""
    cmd.orig = repr(clt)
    cmd.txt = txt
    clt.handle(cmd)
    cmd.wait()
    return cmd
