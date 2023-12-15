#!/usr/bin/python3

def memo(func):
	cache = dict()
	def wrapper(arg1,arg2,arg3):
		if (arg1,arg2,arg3) not in cache:
			cache[(arg1,arg2,arg3)] = func(arg1,arg2,arg3)
		return cache[(arg1,arg2,arg3)]
	return wrapper

@memo
def validator(pattern_o,check_o,parsed_o):
	pattern = list(pattern_o)
	check = list(check_o)
	parsed = list(parsed_o)
	solutions = 0
	
	while len(pattern):
		char = pattern.pop()
		if char == '#':
			parsed.insert(0,'#')
			if len(parsed) > check[-1]:
				return 0
		elif char == '.':
			if len(parsed) == 0:
				continue
			if len(parsed) == check[-1]:
				check.pop()
				if len(check) == 0:
					if '#' in pattern:
						return 0
					else:
						return 1
				parsed = list()
			else:
				return 0
		elif char == '?':
			pattern.append('.')
			solutions += validator(tuple(pattern),tuple(check),tuple(parsed))
			pattern[-1:] = '#'
			solutions += validator(tuple(pattern),tuple(check),tuple(parsed))
			return solutions
	return 0
	

def main(input_file):
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for line in input_lines:
		pattern_five = '.'+((line.split()[0]+"?")*5)[:-1]
		check_five = [int(x) for x in ((line.split()[1]+",")*5).split(',')[:-1]]
		result += validator(tuple(pattern_five),tuple(check_five),tuple())

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 525152,"Test failed, expected 525152, result "+str(test_value)
	print(main("INPUT"))
