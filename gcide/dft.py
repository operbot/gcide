# This file is placed in the Public Domain.


"default"


from .obj import Object


def __dir__():
    return (
            "Default",
           )


class Default(Object):

    __default__ = ""
    
    def __getattr__(self, key):
        try:
            self[key] = Object.__getattr__(self, key)
        except AttributeError:
            self[key] = Default.__default__
        return self[key]
