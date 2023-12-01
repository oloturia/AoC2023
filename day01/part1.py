#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for line in input_lines:
		number = ""
		for c in line:
			if ord(c) >= 48 and ord(c) <= 57:
				number += c
				break
		for c in line[::-1]:
			if ord(c) >= 48 and ord(c) <= 57:
				number += c
				break			
		
		result += int(number)
	return result

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 142,"Test failed, expected 142, result "+str(test_value)
	print(main("INPUT"))
