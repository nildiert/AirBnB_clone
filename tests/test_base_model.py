#!/usr/bin/python3
from models.base_model import BaseModel
#from models import storage
import os
import unittest
import pep8
from datetime import datetime

class TestBaseModel(unittest.Testcase):
    """ Test BaseModel class """

    @classmethod
    def SetUpClass(cls):
        """ Setting  object of class method """
        cls.obj = BaseModel()

    def tearDown(cls):
        """ Delete instances """
        del cls.obj
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        pep_8 = pep8.StyleGuide(quiet=True)
        answ = pep_8.check_files(['models/base_model.py'])
        self.assertEqual(answ.total_errors, 0, "Fix Style")

if __name__ == "__main__":
    unitteest.main()
