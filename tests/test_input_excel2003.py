import unittest

from inputs.excel2003 import excel2003

class TestInputExcel2003(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_simple_spreadsheet(self):
		i = excel2003('tests/assets/inputs_excel2003_test_simple_spreadsheet.xls')
		self.assertEqual(i.next(), ["a", "b", "c",   ""])
		self.assertEqual(i.next(), ["1",  2., "3",   ""])
		self.assertEqual(i.next(), [ 7., "8",  9., "10"])
		self.assertRaises(StopIteration, i.next)
