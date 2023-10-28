#
import unittest
from src.homework.g_lists_and_tuples.lists import add_inventory, remove_inventory_widget


class Test_Config(unittest.TestCase):
     def test_add_inventory(self):
             inventory_dictionary = {} 
             add_inventory(inventory_dictionary, 'Widget1', 10)
             self.assertEqual(inventory_dictionary['Widget1'], 10)
             add_inventory(inventory_dictionary, 'Widget1', 25)
             self.assertEqual(inventory_dictionary['Widget1'], 35)
             add_inventory(inventory_dictionary, 'Widget1', -10)
             self.assertEqual(inventory_dictionary['Widget1'], 25)

     def test_remove_inventory_widget(self): 
        inventory = {"Widget1": 10, "Widget2": 20}
        self.assertEqual(len(inventory), 2)
        self.assertEqual(remove_inventory_widget(inventory, 'Widget1'), 'Record Deleted')
        self.assertEqual(len(inventory), 1)
        self.assertEqual(remove_inventory_widget(inventory, 'Widget1'), "Item Not Found")
        self.assertEqual(inventory, {'Widget2': 20})
        print(inventory)
     

    

 



            
            
          
