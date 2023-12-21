#!/usr/bin/python3

def main(input_file,steps):
	matrix = list()
	start = tuple()
	with open(input_file) as f:
		for y,line in enumerate(f.readlines()):
			matrix.append(list())
			for x,char in enumerate(line.rstrip()):
				if char == 'S':
					start = (x,y)
					matrix[y].append('.')
				else:
					matrix[y].append(char)

	pos = set()
	pos.add(start)
	for i in range(steps):
		npos = set()
		for p in pos:
			x = p[0]
			y = p[1]
			for xm,ym in zip((-1,0,1,0),(0,-1,0,1)):
				if matrix[y+ym][x+xm] == '.':
					npos.add((x+xm,y+ym))
		pos = npos
	return len(pos)

if __name__ == "__main__":
	test_value = main("TEST",6)
	assert test_value == 16,"Test failed, expected 16, result "+str(test_value)
	print(main("INPUT",64))
