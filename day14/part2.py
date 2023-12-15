#!/usr/bin/python3

def cycle(lines):
	for _ in range(0,4):
		north_limit = dict()
		for i in range(0,len(lines[0])):
			north_limit[i] = 0
		rock_coord = set()
		for row,line in enumerate(lines):
			for col,char in enumerate(line):
				if char == '#':
					north_limit[col] = row+1
				elif char == 'O':
					rock_coord.add((north_limit[col],col))
					north_limit[col] += 1
		for row in enumerate(lines):
			lines[row[0]] = "".join(lines[row[0]])
			lines[row[0]] = lines[row[0]].replace('O','.')
		for rock in rock_coord:
			lines[rock[0]] = lines[rock[0]][:rock[1]] +'O' + lines[rock[0]][rock[1]+1:]
		lines = list(zip(*lines[::-1]))	
	return lines
	
	
def main(input_file):
	with open(input_file) as f:
		input_lines = [tuple(line.rstrip()) for line in f.readlines()]
    
	cycles = 1_000_000_000
	history = dict()

	i = 0
	while True:
		history[hash(tuple(input_lines))] = i
		input_lines = cycle(input_lines)
		if hash(tuple(input_lines)) in history:
			cycle_start = history[hash(tuple(input_lines))]
			cycle_len = i - cycle_start
			
			break
		i += 1
	
	cycles = (cycles-1)%cycle_len
	for i in range(0,cycles):
		input_lines = cycle(input_lines)
	result = 0
	
	for row,line in enumerate(input_lines):
		for col in line:
			if col == 'O':
				result += len(input_lines)-row
	return 	result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 64,"Test failed, expected 64, result "+str(test_value)
	print(main("INPUT"))
