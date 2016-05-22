import unittest
import os
import xlrd

from recipes.simple_table_rowmerger import simple_table_rowmerger

class TestRecipeSimpleTableRowmerger(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_keys_not_provided(self):
		mg = simple_table_rowmerger([[], []], {'nokey': True})
		self.assertRaises(Exception, mg.next)
		
	def test_keys_provided_with_wrong_type(self):
		mg = simple_table_rowmerger([[], []], {'keys': True})
		self.assertRaises(Exception, mg.next)
		
	def test_keys_provided_with_partially_wrong_type(self):
		mg = simple_table_rowmerger([[], []], {'keys': [1, {}]})
		self.assertRaises(Exception, mg.next)
		
	def test_keys_provided_with_partially_wrong_length(self):
		mg = simple_table_rowmerger([[], []], {'keys': [1, 0, 1]})
		self.assertRaises(Exception, mg.next)
		
	def test_simple_merge(self):
		LEFT_TABLE = [
			["1", "a", "b", "c"],
			["3", "d", "e", "f"],
			["4", "g", "h", "i"],
			["5", "j", "k", "l"],
			["6", "m", "n", "o"],
			["7", "p", "q", "r"],
		]
		RIGHT_TABLE = [
			["2", "D", "E", "F"],
			["3", "G", "H", "I"],
			["4", "J", "K", "L"],
		]
			
		PARAMS = {"keys": [0, 0]}
		mg = simple_table_rowmerger([LEFT_TABLE, RIGHT_TABLE], PARAMS)
		self.assertEquals(mg.next(), ["1", "a", "b", "c",  "",  "",  ""])
		self.assertEquals(mg.next(), ["2",  "",  "",  "", "D", "E", "F"])
		self.assertEquals(mg.next(), ["3", "d", "e", "f", "G", "H", "I"])
		self.assertEquals(mg.next(), ["4", "g", "h", "i", "J", "K", "L"])
		self.assertEquals(mg.next(), ["5", "j", "k", "l",  "",  "",  ""])
		self.assertEquals(mg.next(), ["6", "m", "n", "o",  "",  "",  ""])
		self.assertEquals(mg.next(), ["7", "p", "q", "r",  "",  "",  ""])
		self.assertRaises(StopIteration, mg.next)
