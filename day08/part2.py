#!/usr/bin/python3
import numpy

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
	
	start_pos = [c for c in dmap if c[2] == 'A']
	pos_dest = list()
		
	for cur_pos in start_pos:
		pos = cur_pos
		steps = 0	
		while pos[2] != 'Z':
			pos = dmap[pos][istr[steps%(len(istr))]]
			steps += 1
		pos_dest.append(steps)
		
	result = numpy.lcm.reduce(pos_dest)

	return result

if __name__ == "__main__":
	test_value = main("TEST2")
	assert test_value == 6,"Test failed, expected 6, result "+str(test_value)
	print(main("INPUT"))
