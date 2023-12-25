#!/usr/bin/python3
areaA = 0
areaB = 0

def intersect(p1x,p1y,n1x,n1y,p2x,p2y,n2x,n2y):
	global areaA
	global areaB
	
	p1xEnd = p1x + n1x
	p1yEnd = p1y + n1y
	
	p2xEnd = p2x + n2x
	p2yEnd = p2y + n2y
	
	m1 = (p1yEnd - p1y) / (p1xEnd - p1x)
	m2 = (p2yEnd - p2y) / (p2xEnd - p2x)
	
	b1 = p1y - m1 * p1x
	b2 = p2y - m2 * p2x
	
	try:
		px = (b2-b1) / (m1-m2)
	except ZeroDivisionError:
		return 0
	py = m1*px+b1
	
	if areaA <= px <= areaB and areaA <= py <= areaB:
		if ((n1x < 0 and px > p1x) or (n1x > 0 and px < p1x)) or ((n2x < 0 and px > p2x) or (n2x > 0 and px < p2x)) or  ((n1y < 0 and py > p1y) or (n1y > 0 and py < p1y)) or ((n2y < 0 and py > p2y) or (n2y > 0 and py < p2y)):
			return 0	
		return 1
	else:
		return 0


def main(input_file,areaAdef,areaBdef):
	global areaA
	global areaB
	
	areaA = areaAdef
	areaB = areaBdef
	hpos = list()
	with open(input_file) as f:
		for line in f.readlines():
			hpos.append( {'x':int(line.rstrip().split(",")[0]),'y':int(line.rstrip().split(",")[1]),'dx':int(line.rstrip().split("@")[1].split(",")[0]),'dy':int(line.rstrip().split("@")[1].split(",")[1])} )
	
	result = 0
	
	for a,line1 in enumerate(hpos):
		for b,line2 in enumerate(hpos):
			if b > a:		
				result += intersect(line1['x'],line1['y'],line1['dx'],line1['dy'],line2['x'],line2['y'],line2['dx'],line2['dy'])

	return result

if __name__ == "__main__":
	test_value = main("TEST",7,27)
	assert test_value == 2,"Test failed, expected 2, result "+str(test_value)
	print(main("INPUT",200000000000000,400000000000000))
