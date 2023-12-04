#!/usr/bin/python3

def main(input_file):
	result = 0
	cards = list()
	with open(input_file) as f:
		for line in f.readlines():
			winning_numbers = line.rstrip().split(":")[1].split("|")[0].split()
			card_numbers = line.rstrip().split(":")[1].split("|")[1].split()
			score = 0
			for num in winning_numbers:
				if num in card_numbers:
					score += 1
			cards.append( {"quantity":1, "winning":score}  )		
			
	for i1,card in enumerate(cards):
		result += card["quantity"]
		for i2 in range(1,card["winning"]+1):
			cards[i1+i2]["quantity"] += 1*cards[i1]["quantity"]
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 30,"Test failed, expected 30, result "+str(test_value)
	print(main("INPUT"))
