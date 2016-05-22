import xlrd

def excel2003(filepath):
	book = xlrd.open_workbook(filepath)
	sheet = book.sheet_by_index(0)
	ncols = sheet.ncols
	for row_index in range(sheet.nrows):
		row_values = sheet.row_values(row_index)
		row_values.extend( [""] * (ncols - len(row_values)) )
		yield row_values
	
