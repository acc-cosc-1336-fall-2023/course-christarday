
import unittest
from src.homework.h_strings.strings import get_dna_complement, get_hamming_distance
class Test_Config(unittest.TestCase): 

 class TestGetHammingDistance(unittest.TestCase):


      def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7)
        self.assertEqual(get_hamming_distance('1', '1'), 0)
        self.assertEqual(get_hamming_distance('11', '1'), "Invalid, both strings are not of equal length")

      def  test_get_dna_complement(self):
         self.assertEqual(get_dna_complement('AAAACCCGGT'), 'ACCGGGTTTT')
         self.assertEqual(get_dna_complement('ACGTY'), 'This sequence is not a DNA strand.')
                          
                          

 