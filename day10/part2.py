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
	current_char = 'S'
	while True:
		pos['y'],pos['x'] = check_boundaries(pos,input_lines,conn,last_pos)
		if(pos['y'] == -1 and pos['x'] == -1):
			break
		last_pos.append((pos['y'],pos['x']))
		current_char = input_lines[pos['y']][pos['x']]
	
	row = 0
	while row < len(input_lines):
		new_line = ""
		for col,sec in enumerate(input_lines[row]):
			if (row,col) not in last_pos:
				new_line += "."
			else:
				new_line += sec
		input_lines[row] = new_line
		row += 1
	
	new_map = list()
	index = -1
	row = 0
	
	while row < len(input_lines):
		new_map.append(list())
		index +=1	
		for i,sec in enumerate(input_lines[row][:-1]):
			nsec = input_lines[row][i+1]
			if (sec == 'F' or sec == 'L' or sec == '-' or sec == 'S') and (nsec == '7' or nsec == '-' or nsec == 'J' or nsec == 'S'):
				new_map[index] += sec+'-'
			else:
				new_map[index] += sec+','
		new_map[index] += nsec
		new_map.append(list())
		index += 1
		row += 1
		
	row = 1
	while row < len(new_map)-1:
		if len(new_map[row]) == 0:
			for i,psec in enumerate(new_map[row-1]):
				nsec = new_map[row+1][i]
				if (psec == 'F' or psec == '7' or psec == '|' or psec == 'S') and (nsec == 'J' or nsec == 'L' or nsec == '|' or nsec == 'S'):
					new_map[row] += '|'
				else:
					new_map[row] += ','
		row +=1
		
	new_map.pop()
	subst = False
	while not subst:
		subst = True
		row = 0
		while row < len(new_map):
			new_line = ""
			for col,sec in enumerate(new_map[row]):	
				if sec == '.'  or sec == ',':
					if row == 0 or row == len(new_map)-1 or col == 0 or col == len(new_map[row])-1:
						new_line += 'O'
						subst = False
					else:
						if new_map[row-1][col] == 'O' or new_map[row+1][col] == 'O' or new_map[row][col-1] == 'O' or new_map[row][col+1] == 'O':
							new_line += 'O'
							subst = False
						else:
							new_line += sec					
				else:
					new_line += sec
				
			new_map[row] = new_line
			row += 1
			
	result = 0
	for line in new_map:
		result += line.count('.')
	
	return result

if __name__ == "__main__":
	test_value = main("TEST2")
	assert test_value == 10,"Test failed, expected 10, result "+str(test_value)
	print(main("INPUT"))
	
