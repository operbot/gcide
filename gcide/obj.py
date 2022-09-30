# This file is placed in the Public Domain.
# pylint: disable=W0613


"object"


import datetime
import json
import os
import types


from json import JSONDecoder, JSONEncoder


from .cls import Class
from .utl import cdir, fnclass
from .wdr import Wd


def __dir__():
    return (
            'Object',
            'ObjectDecoder',
            'ObjectEncoder',
            'dump',
            'dumps',
            'loads',
            'name',
            'printable',
           )


class Object:


    __methods__ = {}

    def __init__(self, *args, **kwargs):
        object.__init__(self)
        if args:
            try:
                self.__dict__.update(vars(args[0]))
            except TypeError:
                self.__dict__.update(args[0])

    def __delitem__(self, key):
        self.__dict__.__delitem__(self, key)

    def __getattr__(self, key):
        if key in Object.__methods__:
            return Object.__methods__[key]
        if key in self.__dict__:
            return self.__dict__.get(key)
        raise AttributeError(key)

    def __getitem__(self, key):
        return self.__dict__.__getitem__(key)

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __setattr__(self, key, value):
        if type(value) in [types.MethodType,]:
            Object.__methods__[key] = value
        else:
            self.__dict__[key] = value

    def __setitem__(self, key, value):
        return self.__dict__.__setitem__(key, value)

    def __str__(self):
        return str(self. __dict__)

    def edit(self, setter):
        for key, value in setter.items():
            self[key] =  value

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def items(self):
        if isinstance(self, type({})):
            return self.items()
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def load(self, opath):
        splitted = opath.split(os.sep)
        stp = os.sep.join(splitted[-4:])
        lpath = os.path.join(Wd.workdir, "store", stp)
        if os.path.exists(lpath):
            with open(lpath, "r", encoding="utf-8") as ofile:
                res = json.load(ofile, cls=ObjectDecoder)
                self.update(res)

    def save(self):
        stp = os.path.join(
                           self.type(),
                           os.sep.join(str(datetime.datetime.now()).split())
                          )
        opath = Wd.getpath(stp)
        dump(self, opath)
        os.chmod(opath, 0o444)
        return stp

    def type(self):
        return str(type(self)).split()[-1][1:-2]

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def values(self):
        return self.__dict__.values()


Class.add(Object)


class ObjectDecoder(JSONDecoder):

    def  __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, *args, **kwargs)

    def decode(self, s, _w=None):
        value = json.loads(s)
        return Object(value)

    def raw_decode(self, s, *args, **kwargs):
        return JSONDecoder.raw_decode(self, s, *args, **kwargs)


class ObjectEncoder(JSONEncoder):

    def  __init__(self, *args, **kwargs):
        JSONEncoder.__init__(self, *args, **kwargs)

    def encode(self, o):
        return JSONEncoder.encode(self, o)

    def default(self, o):
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))
                     ):
            return o
        try:
            return JSONEncoder.default(self, o)
        except TypeError:
            return str(o)

    def iterencode(self, o, *args, **kwargs):
        return JSONEncoder.iterencode(self, o, *args, **kwargs)


def name(self):
    typ = type(self)
    if isinstance(typ, types.ModuleType):
        return self.__name__
    if "__self__" in dir(self):
        return "%s.%s" % (self.__self__.__class__.__name__, self.__name__)
    if "__class__" in dir(self) and "__name__" in dir(self):
        return "%s.%s" % (self.__class__.__name__, self.__name__)
    if "__class__" in dir(self):
        return self.__class__.__name__
    if "__name__" in dir(self):
        return self.__name__
    return None




def printable(obj, args="", skip="", plain=False):
    res = []
    keyz = []
    if "," in args:
        keyz = args.split(",")
    if not keyz:
        keyz = obj.keys()
    for key in keyz:
        if key.startswith("_"):
            continue
        if skip:
            skips = skip.split(",")
            if key in skips:
                continue
        value = getattr(obj, key, None)
        if not value:
            continue
        if " object at " in str(value):
            continue
        txt = ""
        if plain:
            txt = str(value)
        elif isinstance(value, str) and len(value.split()) >= 2:
            txt = '%s="%s"' % (key, value)
        else:
            txt = '%s=%s' % (key, value)
        res.append(txt)
    txt = " ".join(res)
    return txt.rstrip()


def dump(obj, opath):
    cdir(opath)
    with open(opath, "w", encoding="utf-8") as ofile:
        json.dump(
            obj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
        )
    return opath


def dumps(obj):
    return json.dumps(obj, cls=ObjectEncoder)


def hook(path):
    cname = fnclass(path)
    cls = Class.get(cname)
    if cls:
        obj = cls()
    else:
        obj = Object()
    load(obj, path)
    return obj


def load(obj, opath):
    splitted = opath.split(os.sep)
    stp = os.sep.join(splitted[-4:])
    lpath = os.path.join(Wd.workdir, "store", stp)
    if os.path.exists(lpath):
        with open(lpath, "r", encoding="utf-8") as ofile:
            res = json.load(ofile, cls=ObjectDecoder)
            obj.update(res)


def loads(jss):
    return json.loads(jss, cls=ObjectDecoder)
