#!/usr/bin/python3



def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	result = 0
	nrs = ["zero","one","two","three","four","five","six","seven","eight","nine"]
	
	
	for line in input_lines:
		
		numberA = ""
		for i,c in enumerate(line):
			if ord(c) >= 48 and ord(c) <= 57:
				numberA += c
				break
			else:
				for pos,n in enumerate(nrs):
					if line[i:i+len(n)] == n:
						numberA = str(pos)
						break
				if numberA != "":
					break

		numberB = ""
		line = line[::-1]
		for i,c in enumerate(line):
			if ord(c) >= 48 and ord(c) <= 57:
				numberB += c
				break
			else:
				for pos,n in enumerate(nrs):
					if line[i:i+len(n)] == n[::-1]:
						numberB = str(pos)
						break
				if numberB != "":
					break
				
		result += int(numberA+numberB)
	return result

if __name__ == "__main__":
	test_value = main("TEST2")
	assert test_value == 281,"Test failed, expected 281, result "+str(test_value)
	print(main("INPUT"))
