def simple_row_merger(input_table, parameters={"key": 0}):
	if 'key' not in parameters.keys() or not isinstance(parameters['key'], int):
		raise Exception("Second argument should have an integer 'key' key")
	key = parameters["key"]
	if 'cols' not in parameters.keys():
		cols = [i for i in range(len(input_table)) if i <> key]
	else:
		cols = parameters['cols']
	line_to_output = None
	for line_num, line in enumerate(input_table):
		if line_to_output is None:
			line_to_output = line
		if line_num < len(input_table)-1:
			next_line = input_table[line_num+1]
			if next_line[key] == line_to_output[key]:
				for col_index, next_line_item in enumerate(next_line):
					if col_index == key:
						pass
					elif col_index in cols:
						line_to_output[col_index] = line_to_output[col_index] + '\n' + next_line_item
			else:
				yield line_to_output
				line_to_output = None
		else:
			yield line_to_output 
