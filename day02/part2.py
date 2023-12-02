#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	
	result = 0

	for i,line in enumerate(input_lines):
		line = line.split(":")[1]
		minimum_set = {"red":0, "green":0, "blue":0}
		for drawn in line.split(";"):
			for colour in drawn.split(","):
				if int(colour.split()[0]) > minimum_set[colour.split()[1]]:
					minimum_set[colour.split()[1]] = int(colour.split()[0])
		
		result += minimum_set["red"]*minimum_set["green"]*minimum_set["blue"]
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 2286,"Test failed, expected 2286, result "+str(test_value)
	print(main("INPUT"))
