#!/usr/bin/python3

def hashbox(string):
	cur_val = 0
	for c in string:
		cur_val += ord(c)
		cur_val *= 17
		cur_val = cur_val % 256
	return cur_val

def main(input_file):
	with open(input_file) as f:
		lines = f.readlines()[0].rstrip().split(",")

	result = 0
	boxes = dict()
	for line in lines:
		if '=' in line:
			label = line.split('=')[0]
			action = line.split('=')[1]
		else:
			label = line[:-1]
			action = '-'
		box = hashbox(label)
		
		if box not in boxes:
			boxes[box] = dict()
			
		if label in boxes[box]:
			if action == '-':
				boxes[box].pop(label)
			else:
				boxes[box][label] = int(action)
		else:
			if action != '-':
				boxes[box][label] = int(action)
		
	for label,box in boxes.items():
		for slot,lens in enumerate(box):
			result += (label+1) * (slot+1) * box[lens]
			
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 145,"Test failed, expected 145, result "+str(test_value)
	print(main("INPUT"))
