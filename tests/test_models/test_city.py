#!/usr/bin/python3
from models.base_model import BaseModel
from models.city import City
import os
import unittest
import pep8
from datetime import datetime


class TestCity(unittest.TestCase):
    """ Test City class """

    @classmethod
    def setUpClass(cls):
        """ Setting instance of method """
        cls.inst = City()

    @classmethod
    def teardown(cls):
        """ Delete instances  """
        del cls.inst
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8(self):
        """ Pep8 test """
        pep_8 = pep8.StyleGuide(quiet=True)
        answ = pep_8.check_files(['models/city.py'])
        self.assertEqual(answ.total_errors, 0, "Fix Style")

    def test_instance(self):
        """ Verify instance """
        self.assertTrue(isinstance(self.inst,City))

    def test_has_attribute(self):
        """ Test attributes """
        self.assertTrue(hasattr(City, "save"))
        self.assertTrue(hasattr(City, "to_dict"))
        self.assertTrue(hasattr(City, "__str__"))
        self.assertTrue(hasattr(City, "__init__"))

    def test_docstring(self):
        """ Test docstring """
        self.assertIsNotNone(City.__doc__)

    def test_dict_doc(self):
        """ test docstring of each method """
        for doc in dir(City):
            self.assertIsNotNone(doc.__doc__)

    def test_save(self):
        """ Test difference between created_at and updated_at """
        self.inst.save()
        self.assertNotEqual(self.inst.created_at, self.inst.updated_at)

    def test_type_datetime(self):
        self.assertEqual(datetime, type(self.inst.created_at))
        self.assertEqual(datetime, type(self.inst.updated_at))

    def test_to_dict(self):
        dict_test = self.inst.to_dict()
        self.assertEqual(dict, type(dict_test))

    def test_type_id(self):
        self.assertEqual(str, type(self.inst.id))

if __name__ == "__main__":
    unittest.main()
