#!/usr/bin/python3

def main(input_file):
	result = 0
	with open(input_file) as f:
		for line in f.readlines():
			winning_numbers = line.rstrip().split(":")[1].split("|")[0].split()
			card_numbers = line.rstrip().split(":")[1].split("|")[1].split()
			score = 0
			for num in winning_numbers:
				if num in card_numbers:
					if score == 0:
						score = 1
					else:
						score *= 2
			result += score
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 13,"Test failed, expected 13, result "+str(test_value)
	print(main("INPUT"))
