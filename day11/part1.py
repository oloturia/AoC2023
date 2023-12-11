#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [[c for c in line.rstrip()] for line in f.readlines()]

	i1 = 0
	row_expand = set()
	while i1 < len(input_lines):
		if '#' not in input_lines[i1]:
			input_lines.insert(i1,['.']*len(input_lines[i1]))
			i1 += 1
		else:
			for i2,c in enumerate(input_lines[i1]):
				if c == '#':
					row_expand.add(i2)
		i1 += 1
	
	i1 = 0
	while i1 < len(input_lines):
		for i2 in range(len(input_lines[i1])-1,-1,-1):
			if i2 not in row_expand:
				input_lines[i1].insert(i2,'.')
		i1 += 1
	
	coords = list()
	for row,line in enumerate(input_lines):
		for col,char in enumerate(line):
			if char == '#':
				coords.append((row,col))

	result = 0
	for i,gal_a in enumerate(coords):
		for gal_b in coords[i:]:
			result += abs(gal_a[0] - gal_b[0]) + abs(gal_a[1] - gal_b[1])
				
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 374,"Test failed, expected 374, result "+str(test_value)
	print(main("INPUT"))
