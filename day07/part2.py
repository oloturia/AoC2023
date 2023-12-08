#!/usr/bin/python3

def calc_power(house):
	equals = list()
	prev_crd = 0
	power = 0
	house.sort()
	count_eq = 0
	for crd in house:
		if prev_crd == 0:
			prev_crd = crd
		else:
			if prev_crd == crd:
				count_eq += 1
			else:
				prev_crd = crd
				if count_eq > 0:
					equals.append(count_eq)
				count_eq = 0
	if count_eq > 0:
		equals.append(count_eq)	
	if equals == [4]:
		return 6
	elif equals == [3]:
		return 5
	elif equals == [2,1] or equals == [1,2]:
		return 4
	elif equals == [2]:
		return 3
	elif equals == [1,1]:
		return 2
	elif equals == [1]:
		return 1
	else:
		return 0

def reord(origin):
	indexer = lambda x : 10 if x == 'T' else (1 if x == 'J' else (12 if x == 'Q' else (13 if x == 'K' else (14 if x == 'A' else (int(x))))))
	new = list()
	for o in origin:
		new.append( indexer(o) )
	return new

def main(input_file):
	with open(input_file) as f:
		input_lines = [[reord(line.rstrip().split()[0]),int(line.rstrip().split()[1]) ] for line in f.readlines()]
		
	ranks = len(input_lines)
	result = 0
	five_of_a_kind = list()
	four_of_a_kind = list()
	full_house = list()
	three_of_a_kind = list()
	two_pair = list()
	one_pair = list()
	high_card = list()
	
	for i1 in input_lines:
		
		max_power = 0
		count_jokers = i1[0].count(1)
		
		if count_jokers == 5 or count_jokers == 4:
			five_of_a_kind.append(i1)
		elif count_jokers == 3:
			other_cards = set(i1[0])
			other_cards.remove(1)
			if len(other_cards) == 1:
				five_of_a_kind.append(i1)
			else:
				four_of_a_kind.append(i1)
		elif count_jokers == 2:
			other_cards = set(i1[0])
			other_cards.remove(1)
			if len(other_cards) == 1:
				five_of_a_kind.append(i1)
			elif len(other_cards) == 2:
				four_of_a_kind.append(i1)
			elif len(other_cards) == 3:
				three_of_a_kind.append(i1)
		else:
			if count_jokers == 0:
				max_power = calc_power( i1[0].copy() )
			else:
				wildcards = set(i1[0])
				wildcards.remove(1)
				for comb in wildcards:
					temp_hand = i1[0].copy()
					temp_hand[temp_hand.index(1)] = comb
					power = calc_power(temp_hand)
					if power > max_power:
						max_power = power
						
			if max_power == 6:
				five_of_a_kind.append(i1)
			elif max_power == 5:
				four_of_a_kind.append(i1)
			elif max_power == 4:
				full_house.append(i1)
			elif max_power == 3:
				three_of_a_kind.append(i1)
			elif max_power == 2:
				two_pair.append(i1)
			elif max_power == 1:
				one_pair.append(i1)
			else:
				high_card.append(i1)
				
	five_of_a_kind.sort(reverse=True)
	for i in five_of_a_kind:
		result += ranks * i[1]
		ranks -= 1
	four_of_a_kind.sort(reverse=True)
	for i in four_of_a_kind:
		result += ranks * i[1]
		ranks -= 1
	full_house.sort(reverse=True)
	for i in full_house:
		result += ranks * i[1]
		ranks -= 1	
	three_of_a_kind.sort(reverse=True)
	for i in three_of_a_kind:
		result += ranks * i[1]
		ranks -= 1
	two_pair.sort(reverse=True)
	for i in two_pair:
		result += ranks * i[1]
		ranks -= 1
	one_pair.sort(reverse=True)
	for i in one_pair:
		result += ranks * i[1]
		ranks -= 1
	high_card.sort(reverse=True)
	for i in high_card:
		result += ranks * i[1]
		ranks -= 1				
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 5905,"Test failed, expected 5905, result "+str(test_value)
	print(main("INPUT"))
