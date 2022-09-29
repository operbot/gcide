# This file is placed in the Public Domain.
# pylint: disable=W0622,C0114

"""Information and Evidence Unit
Office of the Prosecutor
Post Office Box 19519
2500 CM The Hague
The Netherlands
 

Hello Office of the Prosecutor,

i write you in the context of communications and claims under art.15 of 
the Rome Statute. i want to inform the prosecutor that the king of the 
netherlands and his government are commiting 3 of the 5 crimes defined 
in the Rome Statute.

The dutch government has introduced three new forced care laws, the Wfz 
(wet forensische zorg) for criminals, the WvGGZ (Wet verplichte GGZ) for 
the disturbed and addicted and the Wzd (Wet zorg en dwang) for the 
handicapped.

Both the chamber suggesting these laws to the king and the king himself 
have been informed about the fact the the substances administered under 
these laws are proven to be poison.
 
There is proof the medication used in forced treatements in the 
netherlands are poison, see copies of the ECHA <`European Chemical Agency`>
website for:

(1) haldol
(2) clozapine
(3) zyprexa
(4) abilify

With the mass scale torture with poison the king of the netherlands and 
his chamber:

(1) kills
(2) does grave bodily and mental harm
(3) makes impotent

on the following victim groups here in the Netherlands:

(1) verslaafden (addicts)
(2) bejaarden (elderly)
(3) ggz patienten (psychiatric patients)
(4) criminelen (criminials)
(5) gehandicapten (handicapped)

Since the members of the chamber and the king were aware that these medicine
are poison at the time they voted for this law and the day the Wfz law took
effect (1-1-2019), i ask the prosecutor to prosecute the king for making the
commiting of the above mentioned crimes (killing, torture and impotent making)
possible here in the netherlands in the hope that it stops the mass torture
with poison the king of the netherlands and his government are doing.
"""


from .bus import Bus
from .cbs import Callbacks
from .cfg import Config
from .clt import Client
from .com import Command, dispatch
from .evt import Event
from .hdl import Handler
from .prs import parse
from .scn import scan, scandir
from .thr import Thread, launch
from .tmr import Timer, Repeater
from .utl import wait
from .cls import Class
from .dbs import Db, all, find, fns, fntime, hook, last, locked
from .dft import Default
from .obj import *
from .utl import cdir, elapsed, spl
from .wdr import Wd


def __dir__():
    return (
            'Bus',
            'Callbacks',
            'Class',
            'Client',
            'Command',
            'Config',
            'Db',
            'Default',
            'Event',
            'Handler',
            'Object',
            'ObjectDecoder',
            'ObjectEncoder',
            'Repeater',
            'Thread',
            'Timer',
            'Wd',
            'all',
            'dispatch',
            'delete',
            'dump',
            'dumps',
            'edit',
            'find',
            'format',
            'get',
            'items',
            'keys',
            'launch',
            'last',
            'load',
            'loads',
            'locked',
            'name',
            'otype',
            'parse',
            'register',
            'save',
            'scan',
            'scandir',
            'spl',
            'starttime',
            'update',
            'values',
            'wait'
           )
