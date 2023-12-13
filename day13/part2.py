#!/usr/bin/python3

def count_error(alin,blin):
	errors = 0
	for a,b in zip(alin,blin):
		if a != b:
			errors += 1
	return errors

def analyze(maps):
	symm = dict()
	for x in range(1,len(maps[0])):
		symm[x] = 0
	for row,line in enumerate(maps):
		for i in range(1,len(maps[0])):
			if symm[i] <= 1:
				if(len(line[:i]) <= len(line[i:][::-1])):
					symm[i] += count_error(line[:i], line[i:i+len(line[:i])][::-1])	
				else:
					symm[i] += count_error(line[i-len(line[i:]):i], line[i:][::-1])
	for x in symm:
		if symm[x] == 1:
			return x
	return 0
			
def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	maps = list()
	result = 0
	for i,line in enumerate(input_lines):
		if len(line) == 0 or i == len(input_lines)-1:
			result += analyze(tuple(maps))
			result += analyze(list(zip(*maps)))*100
			maps = list()
		else:
			maps.append( line )

	return 	result

if __name__ == "__main__":

	test_value = main("TEST")
	assert test_value == 400,"Test failed, expected 400, result "+str(test_value)
	print(main("INPUT"))
