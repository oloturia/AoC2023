#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	dmap = dict()
	istr = list()
	for line in input_lines:
		if '=' in line:
			dmap[line.split(" = ")[0]] = line.split(" = ")[1][1:-1].split(", ")
		elif len(line) > 0:
			istr = [0 if c == 'L' else 1 for c in line]
	
	pos = "AAA"
	steps = 0
	while pos != "ZZZ":
		pos = dmap[pos][istr[steps%(len(istr))]]
		steps += 1
	
	return steps

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 6,"Test failed, expected 6, result "+str(test_value)
	print(main("INPUT"))
