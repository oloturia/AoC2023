#!/usr/bin/python3

top_ener = 0

def beam_calculator(start_point):
	global input_lines
	global top_ener
	
	directions = {0:{'x':0,'y':-1,'/':90,'\\':270,'|':0,'-':(90,270)}, 90:{'x':1,'y':0,'/':0,'\\':180,'|':(0,180),'-':0}, 180:{'x':0,'y':1,'/':270,'\\':90,'|':0,'-':(90,270)}, 270:{'x':-1,'y':0,'/':180,'\\':0,'|':(0,180),'-':0}, 4:{'x':0,'y':0,'/':4,'\\':4,'|':0,'-':0}}
	beams = [{'x':start_point['x'],'y':start_point['y'],'d':start_point['d']}]
	energized = {(start_point['x'],start_point['y'])}
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
			
	if len(energized) > top_ener:
		top_ener = len(energized)
	return


def main(input_file):
	global input_lines
	global top_ener
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	top_ener = 0
	for x in range(0,len(input_lines[0])):
		beam_calculator({'x':x,'y':0,'d':180})
		beam_calculator({'x':x,'y':len(input_lines)-1,'d':0})
	for y in range(0,len(input_lines)):
		beam_calculator({'x':0,'y':y,'d':90})
		beam_calculator({'x':len(input_lines[0])-1,'y':y,'d':270})

	return top_ener

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 51,"Test failed, expected 51, result "+str(test_value)
	print(main("INPUT"))
