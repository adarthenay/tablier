def get_item_or_none(itr):
	try:
		ret = itr.next()
	except StopIteration:
		ret = None
	return ret

def simple_row_merger(input_table, parameters={"key": 0}):
	if 'key' not in parameters.keys() or not isinstance(parameters['key'], int):
		raise Exception("Second argument should have an integer 'key' key")
	key = parameters["key"]
	cols = None

	input_table = iter(input_table)
	current_row = get_item_or_none(input_table)

	while current_row is not None:
		if cols is None:
			if 'cols' not in parameters.keys():
				cols = [i for i in range(len(current_row)) if i <> key]
			else:
				cols = parameters['cols']

		next_row = get_item_or_none(input_table)

		while next_row is not None and next_row[key] == current_row[key]:
			for idx in cols:
				current_row[idx] = current_row[idx] + '\n' + next_row[idx]
			next_row = get_item_or_none(input_table)
		yield current_row

		if next_row is not None and next_row[key] <> current_row[key]:
			current_row = next_row
		else:
			current_row = get_item_or_none(input_table)
