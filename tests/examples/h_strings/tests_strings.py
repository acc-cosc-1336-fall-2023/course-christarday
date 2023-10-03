import unittest

from src.examples.h_strings.strings import concat_strings, slice_string, slice_w_step_value, test_config 

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc", "def"), "abcdef")

    
    def test_slice_string(self):
        name = "Patty Lynn Smith"
        self.assertEqual(slice_string(name), "Lynn")
        self.assertEqual(name[11:],"Smith") 

    def test_slice_w_step_value(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(slice_w_step_value(letters), "ACEGIKMOQSUWY")

 
        



