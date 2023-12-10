#!/usr/bin/python3

def check_boundaries(curr_pos,pipes,conn,prev_pos):
	cur_conn = pipes[curr_pos['y']][curr_pos['x']]
	
	for next_coord in conn[cur_conn]:
		if (next_coord[0]+curr_pos['y'],next_coord[1]+curr_pos['x']) in prev_pos:
			continue
		
		next_conn = pipes[ curr_pos['y'] + next_coord[0] ][ curr_pos['x'] + next_coord[1] ]
		if next_conn == '.':
			continue
		
		if (next_coord[0]*-1, next_coord[1]*-1) in conn[next_conn]:
			return (curr_pos['y'] + next_coord[0], curr_pos['x'] + next_coord[1] )
	return (-1,-1)
	
def main(input_file):
	pos = {'y':0,'x':0}
	found = False
	input_lines = list()
	with open(input_file) as f:
		for line in f.readlines():
			input_lines.append( line.rstrip() )
			if not found:
				if 'S' in line.rstrip():
					pos['x'] = line.rstrip().index('S')
					found = True
				else:
					pos['y'] += 1
		
	N = (-1,0)
	S = (1,0)
	E = (0,1)
	W = (0,-1)
	
	conn = {'|':[N,S], '-':[W,E], 'L':[N,E], 'J':[N,W], '7':[S,W], 'F':[S,E], 'S':[N,S,E,W]}
	
	last_pos = list()
	steps = 0
	current_char = 'S'
	while True:
		pos['y'],pos['x'] = check_boundaries(pos,input_lines,conn,last_pos)
		if(pos['y'] == -1 and pos['x'] == -1):
			break
		last_pos.append((pos['y'],pos['x']))
		steps += 1
		current_char = input_lines[pos['y']][pos['x']]
		
	return steps//2

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 8,"Test failed, expected 8, result "+str(test_value)
	print(main("INPUT"))
