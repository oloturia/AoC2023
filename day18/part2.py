#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	coord = {'x':0,'y':0}
	coords = list()
	coords.append((0,0))
	perim = 0
	
	for i,line in enumerate(input_lines):
		direction = line.split()[2][7:8]
		length = int( line.split()[2][2:7],16 )
		perim += length
		
		if direction == '0':
			coord['x'] += length
		elif direction == '2':
			coord['x'] -= length
		elif direction == '1':
			coord['y'] -= length
		elif direction == '3':
			coord['y'] += length
		coords.append(tuple((coord['x'],coord['y'])))
	
	r1 = 0
	r2 = 0
	for i in range(len(coords)-1):
		r1 += coords[i][0] * coords[i+1][1]
		r2 += coords[i][1] * coords[i+1][0]

	return ( abs(r1-r2)//2 ) + perim//2 +1

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 952408144115,"Test failed, expected 952408144115, result "+str(test_value)
	print(main("INPUT"))
