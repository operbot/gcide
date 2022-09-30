# This file is placed in the Public Domain.


"test persistence"


import unittest


from gcide import Object


class TestPersist(unittest.TestCase):


    def test_methodoverwrite(self):
        obj = Object()
        print(dir(obj))
        