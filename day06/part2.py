#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	race = int( "".join(input_lines[0].split(":")[1].split()) )
	record = int( "".join(input_lines[1].split(":")[1].split()) )

	wins = 0
	
	for time in range(race//2,0,-1):
		dist = (race - time) * time
		if dist > record:
			wins += 1
		else:
			break
	if race%2 == 0:
		return (wins*2)-1
	else:
		return wins*2 

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 71503,"Test failed, expected 71503, result "+str(test_value)
	print(main("INPUT"))
