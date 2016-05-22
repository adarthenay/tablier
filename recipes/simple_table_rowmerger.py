DEFAULT_PARAMS = {"keys": [0, 0]}

def simple_table_rowmerger(tables, parameters=DEFAULT_PARAMS):
	if 'keys' not in parameters.keys() or \
		not isinstance(parameters['keys'], list) or \
		len([u for u in parameters['keys'] if not isinstance(u, int)]) > 0 or \
		len(tables) <> len(parameters['keys']):
		raise Exception("Second argument should have an integer table 'keys' key")
	keys = parameters['keys']
	indexes = [0, 0]
	turn = 0
	while indexes[0] < len(tables[0]) or indexes[1] < len(tables[1]):	
		if indexes[0] < len(tables[0]) and indexes[1] < len(tables[1]) and tables[0][indexes[0]][keys[0]] == tables[1][indexes[1]][keys[1]]:
			yield tables[0][indexes[0]] + [u for (i, u) in enumerate(tables[1][indexes[1]]) if i <> keys[1]]
			indexes[0] += 1
			indexes[1] += 1
		else:
			if turn == 0:
				if indexes[0] < len(tables[0]):
					yield tables[0][indexes[0]] + ["" for (i, u) in enumerate(tables[1][0]) if i <> keys[1]]
			else:
				if indexes[1] < len(tables[1]):
					yield ["" if i <> keys[0] else tables[1][indexes[1]][keys[1]] for (i, u) in enumerate(tables[0][indexes[1]])] + [u for (i, u) in enumerate(tables[1][indexes[1]]) if i <> keys[1]]
			indexes[turn] += 1
			turn = (turn + 1) % len(tables)
