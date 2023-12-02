#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	current_set = {"red":12, "green":13, "blue":14}
	result = 0

	for i,line in enumerate(input_lines):
		line = line.split(":")[1]
		test = True
		for drawn in line.split(";"):
			for colour in drawn.split(","):
				if int(colour.split()[0]) > current_set[colour.split()[1]]:
					test = False
		if test:
			result += i+1
		
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 8,"Test failed, expected 8, result "+str(test_value)
	print(main("INPUT"))
