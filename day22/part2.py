#!/usr/bin/python3

def main(input_file):
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	blocks = dict()
	still_falling = list()
	maxz = 0
	for i,line in enumerate(input_lines):
		xs = int(line.split('~')[0].split(',')[0])
		ys = int(line.split('~')[0].split(',')[1])
		zs = int(line.split('~')[0].split(',')[2])
	
		xe = int(line.split('~')[1].split(',')[0])
		ye = int(line.split('~')[1].split(',')[1])
		ze = int(line.split('~')[1].split(',')[2])

		blocks[i] = { 'x':list(xs+dim for dim in range(xe+1-xs)), 'y':list(ys+dim for dim in range(ye+1-ys)), 'z':list(zs+dim for dim in range(ze+1-zs)) }
		still_falling.append(i)
		if maxz < zs:
			maxz = zs
	
	result = 0
	maxz +=1
	reached = set()
	new_reached = set()
	touch = dict()
	
	while len(still_falling) > 0:
		for z in range(maxz):
			new_reached.clear()
			for i in still_falling:
				if z == blocks[i]['z'][0]:
					if z-1 == 0:
						new_reached.add(i)
						touch[i] = [-1]
					else:
						check = False
						for reach in (reached | new_reached.copy()):
							if z-1 == blocks[reach]['z'][-1] and ( len(set(blocks[i]['y']) & set(blocks[reach]['y']) ) > 0  and len(set(blocks[i]['x']) & set(blocks[reach]['x']) ) > 0 ):
								check = True
								new_reached.add(i)
								if i in touch:
									touch[i].append(reach)
								else:
									touch[i] = [reach]
						if not check:
							blocks[i]['z'] = [ el-1 for el in  blocks[i]['z'] ]

			
			if len(new_reached) > 0:				
				for reach in new_reached:
					still_falling.remove(reach)
					reached.add(reach)
	
	falling_blocks = set()
	result = 0
	for i in blocks:

		falling_blocks.clear()
		falling_blocks.add(i)
		chain = True
		while chain:
			chain = False
			for stand in touch:
				if stand in falling_blocks:
					continue
				if set(falling_blocks) >= set(touch[stand]):
					falling_blocks.add(stand)
					result += 1
					chain = True
		
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 7,"Test failed, expected 7, result "+str(test_value)
	print(main("INPUT"))
