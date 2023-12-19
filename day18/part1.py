#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	hole = dict()
	
	coord = {'x':0,'y':0}
	maxx = 0
	minx = 0
	miny = 0
	maxy = 0
	result = 0
	
	for line in input_lines:
		direction = line.split()[0]
		length = int( line.split()[1] )
		
		if direction == 'R':
			for i in range(length):
				coord['x'] += 1
				if coord['x'] > maxx:
					maxx = coord['x']
				hole.setdefault(coord['y'],list())
				hole[coord['y']].append(coord['x'])
				result +=1
		elif direction == 'L':
			for i in range (length):
				coord['x'] -= 1
				if coord['x'] < minx:
					minx = coord['x']
				hole.setdefault(coord['y'],list())
				hole[coord['y']].append(coord['x'])
				result +=1
		elif direction == 'D':
			for i in range(length):
				coord['y'] += 1
				hole.setdefault(coord['y'],list())
				hole[coord['y']].append(coord['x'])
				if coord['y'] > maxy:
					maxy = coord['y']
				result +=1
		elif direction == 'U':
			for i in range(length):
				coord['y'] -= 1
				hole.setdefault(coord['y'],list())
				hole[coord['y']].append(coord['x'])
				if coord['y'] < miny:
					miny = coord['y']
				result +=1
	
	flooding = True
	new_lava = { (hole[miny][1],miny) }
	flood_lava = set()
	
	while flooding:
		temp_lava = set()
		for lava in new_lava:
			if not ( lava[0] == maxx or lava[0]+1 in hole[lava[1]] or (lava[0]+1,lava[1]) in flood_lava ):
				temp_lava.add((lava[0]+1,lava[1]))
			if not ( lava[0] == minx or lava[0]-1 in hole[lava[1]] or (lava[0]-1,lava[1]) in flood_lava ):
				temp_lava.add((lava[0]-1,lava[1]))
			if not ( lava[1] == maxy or lava[0] in hole[lava[1]+1] or (lava[0],lava[1]+1) in flood_lava ):
				temp_lava.add((lava[0],lava[1]+1))
			if not ( lava[1] == miny or lava[0] in hole[lava[1]-1] or (lava[0],lava[1]-1) in flood_lava ):
				temp_lava.add((lava[0],lava[1]-1))
		if len(new_lava) == 0:
			flooding = False
		for lava in new_lava:
			flood_lava.add(lava)
		new_lava.clear()
		new_lava = temp_lava
			
	result += len(flood_lava)-1
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 62,"Test failed, expected 62, result "+str(test_value)
	print(main("INPUT"))
