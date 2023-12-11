#!/usr/bin/python3

def main(input_file,expansion):
	with open(input_file) as f:
		input_lines = [[c for c in line.rstrip()] for line in f.readlines()]

	i1 = 0
	row_expand = set()
	col_nexpand = set()
	while i1 < len(input_lines):
		if '#' not in input_lines[i1]:
			row_expand.add(i1)
		else:
			for i2,c in enumerate(input_lines[i1]):
				if c == '#':
					col_nexpand.add(i2)
		i1 += 1

	coords = list()
	offy = 0
	for row,line in enumerate(input_lines):
		offx = 0
		if row in row_expand:
			offy += expansion
			continue
		for col,char in enumerate(line):
			if char == '#':
				coords.append( (offy,offx) )
			elif col not in col_nexpand:
				offx += expansion
				continue
			offx += 1
		offy += 1

	result = 0
	for i,gal_a in enumerate(coords):
		for gal_b in coords[i:]:
			result += abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])
				
	return result

if __name__ == "__main__":
	test_value = main("TEST",100)
	assert test_value == 8410,"Test failed, expected 8410, result "+str(test_value)
	print(main("INPUT",1000000))
