import unittest
import os
import xlrd

from outputs.excel2003 import excel2003

class TestOutputExcel2003(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_simple_spreadsheet(self):
		xl = excel2003('tests/products/test_output_excel2003_simple_spreadsheet.xls')
		xl.add(['1',  2., '3'])
		xl.add(['x', 'y', 'z'])
		xl.write()
		
		book = xlrd.open_workbook('tests/products/test_output_excel2003_simple_spreadsheet.xls')
		sheet = book.sheet_by_index(0)
		self.assertEquals(sheet.nrows, 2)
		self.assertEquals(sheet.row_values(0), [u'1',   2., u'3'])
		self.assertEquals(sheet.row_values(1), [u'x', u'y', u'z'])
		
	def tearDown(self):
		os.remove('tests/products/test_output_excel2003_simple_spreadsheet.xls')

		
