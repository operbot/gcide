# pylint: disable=E1101,C0116,E0611
# This file is placed in the Public Domain.


"model"


import unittest


from gcide import Object
from gcide.mdl import oorzaak


class TestModel(unittest.TestCase):

    def test_model(self):
        self.assertEqual(type(oorzaak), Object)
