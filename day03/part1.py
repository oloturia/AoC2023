#!/usr/bin/python3

def check_boundaries(input_lines,temp_pos,temp_number):
	boundaries = list()
	part = False
	for pos in temp_pos:
		for x in range(-1,2):
			for y in range(-1,2):
				boundaries.append((pos[0]+x, pos[1]+y))
	for bound in boundaries:
		try:
			if input_lines[bound[0]][bound[1]] != "." and ( ord(input_lines[bound[0]][bound[1]]) not in range(ord("0"),ord("9")+1) ):
				return int(temp_number)
		except IndexError:
			pass
	return 0

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for row,line in enumerate(input_lines):
		temp_number = ""
		temp_pos = list()
		for col,char in enumerate(line):
			if ord(char) >= ord("0") and ord(char) <= ord("9"):
				temp_number += char
				temp_pos.append( (row,col) )
			else:
				if temp_number != "":
					result += check_boundaries(input_lines,temp_pos,temp_number)
					temp_pos = list()
					temp_number = ""
			if col == len(line)-1 and temp_number != "":
				result += check_boundaries(input_lines,temp_pos,temp_number)
				temp_pos = list()
				temp_number = ""
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 4361,"Test failed, expected 4361, result "+str(test_value)
	print(main("INPUT"))
