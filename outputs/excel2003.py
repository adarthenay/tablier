import xlwt

class excel2003(object):
	def __init__(self, filepath):
		self.filepath = filepath
		self.wb = xlwt.Workbook()
		self.sh = self.wb.add_sheet('tablier')
		self._row = 0
		self._closed = False
		
	def add(self, row):
		for col_index, cell_content in enumerate(row):
			self.sh.write(self._row, col_index, cell_content)
		self._row += 1
		
	def write(self):
		self.wb.save(self.filepath)
	
