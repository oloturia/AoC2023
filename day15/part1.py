#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		lines = f.readlines()[0].rstrip().split(",")

	result = 0
	for line in lines:
		cur_val = 0
		for c in line:
			cur_val += ord(c)
			cur_val *= 17
			cur_val = cur_val % 256
		result += cur_val
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 1320,"Test failed, expected 1320, result "+str(test_value)
	print(main("INPUT"))
