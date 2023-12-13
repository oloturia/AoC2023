#!/usr/bin/python3

def analyze(maps):
	symm = set()
	for x in range(1,len(maps[0])):
		symm.add(x)
	for row,line in enumerate(maps):
		symm_iter = symm.copy()
		for i in symm_iter:
			if i in symm:
				if(len(line[:i]) <= len(line[i:][::-1])):
					if line[:i] != line[i:i+len(line[:i])][::-1]:
						symm.remove(i)
				else:
					if line[i-len(line[i:]):i] != line[i:][::-1]:
						symm.remove(i)
			else:
				break
		if len(symm_iter) == 0:
			return 0
		
	symm_iter = symm.copy()

	for x in symm_iter:
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
	assert test_value == 405,"Test failed, expected 405, result "+str(test_value)
	print(main("INPUT"))
