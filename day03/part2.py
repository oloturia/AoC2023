#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	list_numbers = dict()
	for row,line in enumerate(input_lines):
		temp_number = ""
		temp_pos = list()
		for col,char in enumerate(line):
			if ord(char) >= ord("0") and ord(char) <= ord("9"):
				temp_number += char
				temp_pos.append( (row,col) )
			else:
				if temp_number != "":
					list_numbers[tuple(temp_pos)] = temp_number
					temp_pos = list()
					temp_number = ""
			if col == len(line)-1 and temp_number != "":
				list_numbers[tuple(temp_pos)] = temp_number
				temp_pos = list()
				temp_number = ""
	
	for row,line in enumerate(input_lines):
		for col,char in enumerate(line):
			if char == '*':
				numbers = set()
				for coords in list_numbers:
					for point in coords:
						if (point[0]+1 == row or point[0] == row or point[0]-1 == row  ) and (point[1]+1 == col or point[1] == col or point[1]-1 == col):
							numbers.add(list_numbers[coords])
				if len(numbers) == 2:
					temp_result = 1
					for n in numbers:
						temp_result *= int(n)
					result += temp_result
					
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 467835,"Test failed, expected 467835, result "+str(test_value)
	print(main("INPUT"))
