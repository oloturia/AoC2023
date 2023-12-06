#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	races = dict( zip([int(x) for x in input_lines[0].split(":")[1].split()],[int(y) for y in input_lines[1].split(":")[1].split()] )  )
	result = 1
	
	for race in races:
		wins = 0
		for time in range(race//2,0,-1):
			dist = (race - time) * time
			if dist > races[race]:
				wins += 1
			else:
				break
		if race%2 == 0:
			result *= (wins*2)-1
		else:
			result *= wins*2 
		
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 288,"Test failed, expected 288, result "+str(test_value)
	print(main("INPUT"))
