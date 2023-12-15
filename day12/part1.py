#!/usr/bin/python3

def checker(pattern, check):
	count = 0
	check = [int(x) for x in check.split(",")]
	result = list()
	for c in pattern:
		if c == '#':
			count +=1
		elif c == '.':
			if count > 0:
				result.append(count)
				count = 0
	if count > 0:
		result.append(count)
	return result == check

def main(input_file):
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for line in input_lines:
		bits = line.count('?')
		tot_bits = sum([int(x) for x in line.split()[1].split(",")  ])
		for bit in range(0,2**bits):
			subpattern = bin(bit)[::-1][:-2]
			temp_line = line.split()[0]	
			if subpattern.count("1") == tot_bits - line.count("#"):
				for s in subpattern:
					if s == "1":
						temp_line = temp_line.replace("?","#",1)
					else:
						temp_line = temp_line.replace("?",".",1)
				temp_line = temp_line.replace("?",".")
				if checker(temp_line,line.split()[1]):
					result +=1

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 21,"Test failed, expected 21, result "+str(test_value)
	print(main("INPUT"))
