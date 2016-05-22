import unittest
import os
import xlrd

from recipes.simple_row_merger import simple_row_merger

class TestRecipeSimpleRowMerger(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_key_not_provided(self):
		mg = simple_row_merger([], {'nokey': True})
		self.assertRaises(Exception, mg.next)
		
	def test_simple_merge(self):
		INPUT = [
			["1", "a", "b", "c"],
			["1", "d", "e", "f"],
			["1", "g", "h", "i"],
			["2", "j", "k", "l"],
			["3", "m", "n", "o"],
			["3", "p", "q", "r"],
		]
		PARAMS = {"key": 0}
		mg = simple_row_merger(INPUT, PARAMS)
		self.assertEquals(mg.next(), ["1", "a\nd\ng", "b\ne\nh", "c\nf\ni"])
		self.assertEquals(mg.next(), ["2", "j", "k", "l"])
		self.assertEquals(mg.next(), ["3", "m\np", "n\nq", "o\nr"])
		self.assertRaises(StopIteration, mg.next)
		
	def test_simple_merge_with_select(self):
		INPUT = [
			["1", "a", "b", "c"],
			["1", "d", "e", "f"],
			["1", "g", "h", "i"],
			["2", "j", "k", "l"],
			["3", "m", "n", "o"],
			["3", "p", "q", "r"],
		]
		PARAMS = {"key": 0, "cols": [2, 3]}
		mg = simple_row_merger(INPUT, PARAMS)
		self.assertEquals(mg.next(), ["1", "a", "b\ne\nh", "c\nf\ni"])
		self.assertEquals(mg.next(), ["2", "j", "k", "l"])
		self.assertEquals(mg.next(), ["3", "m", "n\nq", "o\nr"])
		self.assertRaises(StopIteration, mg.next)
