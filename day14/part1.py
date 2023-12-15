#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	north_limit = dict()
	row_count = dict()
	for i in range(0,len(input_lines)):
		row_count[i] = 0
	
	for i in range(0,len(input_lines[0])):
		north_limit[i] = 0
		
	for row,line in enumerate(input_lines):
		for col,char in enumerate(line):
			if char == '#':
				north_limit[col] = row+1
			elif char == 'O':
				row_count[north_limit[col]] += 1
				north_limit[col] += 1
	result = 0
	
	for i in row_count:
		result += row_count[i] * (len(row_count)-i)
	return 	result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 136,"Test failed, expected 136, result "+str(test_value)
	print(main("INPUT"))
