# This file is placed in the Public Domain.


import unittest


from gcide import Object


class TestPersist(unittest.TestCase):


    def test_methodoverwrite(self):
        o = Object()
        print(dir(o))
        