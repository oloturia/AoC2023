#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
		
	directions = {0:{'x':0,'y':-1,'/':90,'\\':270,'|':0,'-':(90,270)}, 90:{'x':1,'y':0,'/':0,'\\':180,'|':(0,180),'-':0}, 180:{'x':0,'y':1,'/':270,'\\':90,'|':0,'-':(90,270)}, 270:{'x':-1,'y':0,'/':180,'\\':0,'|':(0,180),'-':0}, 4:{'x':0,'y':0,'/':4,'\\':4,'|':0,'-':0}}
	beams = [{'x':0,'y':0,'d':90}]
	energized = {(0,0)}
	cache = set()
	while len(beams) > 0:
		new_beams = list()
		for n,beam in enumerate(beams):
			if (beam['x'],beam['y'],beam['d']) in cache:
				beams[n]['d'] = 4
			else:
				cache.add((beam['x'],beam['y'],beam['d']))
				char = input_lines[beam['y']][beam['x']] 
				
				if char == '\\' or char == '/':
					beams[n]['d'] = directions[beam['d']][char]	
				elif char == '-' or char == '|':
					if directions[beam['d']][char] != 0:
						new_beams.append({'x':beam['x'],'y':beam['y'],'d':directions[beam['d']][char][0]})
						new_beams.append({'x':beam['x'],'y':beam['y'],'d':directions[beam['d']][char][1]})
						beams[n]['d'] = 4

				beams[n]['x'] += directions[beam['d']]['x']
				beams[n]['y'] += directions[beam['d']]['y']
				if beam['x'] < 0 or beam['x'] >= len(input_lines[0]) or beam['y'] < 0 or beam['y'] >= len(input_lines):
					beams[n]['d'] = 4
				else:
					energized.add((beam['x'],beam['y']))
					
		old_beams = beams.copy()
		beams.clear()
		for beam in old_beams:
			if beam['d'] != 4:
				beams.append(beam)
			
		for beam in new_beams:
			beams.append(beam)
			
	return len(energized)

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 46,"Test failed, expected 46, result "+str(test_value)
	print(main("INPUT"))
