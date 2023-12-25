#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		maze = [line.rstrip() for line in f.readlines()]

	pos = [{'x':1,'y':0,'lx':0,'ly':0,'s':0,'start':{'x':1,'y':0},'end':False}]
	arrival = {'x':len(maze[0])-2,'y':len(maze)-1}
	slopes = {'>':{'x':1,'y':0},'<':{'x':-1,'y':0},'^':{'x':0,'y':-1},'v':{'x':0,'y':1}}	
	ending = False
	result = 0
	
	while not ending:
		ending = True
		for p in pos:
			if not p['end']:
				deadEnd = True				
				for xof,yof in zip((p['x']-1,p['x'],p['x']+1,p['x']),(p['y'],p['y']-1,p['y'],p['y']+1)):
					if ( xof == p['lx'] and yof == p['ly'] ) or ( xof < 0 or xof >= len(maze[0]) or yof < 0 or yof >= len(maze) ) :
						continue
					if maze[yof][xof] == '.':
						ending = False
						deadEnd = False
						p['lx'] = p['x']
						p['ly'] = p['y']
						p['x'] = xof
						p['y'] = yof
						p['s'] += 1
						break
						
					elif  (p['x'] == arrival['x'] and p['y'] == arrival['y']):
						result = p['s'] if result < p['s'] else result
						p['end'] = True
						
					elif maze[yof][xof] == '>' or maze[yof][xof] == '<' or maze[yof][xof] == '^' or maze[yof][xof] == 'v':
						ending = False
						deadEnd = False

						p['x'] += slopes[maze[yof][xof]]['x']
						p['y'] += slopes[maze[yof][xof]]['y']
						p['lx'] = p['x']
						p['ly'] = p['y']
						p['x'] += slopes[maze[yof][xof]]['x']
						p['y'] += slopes[maze[yof][xof]]['y']
						p['s'] += 2
						p['end'] = True
						
						for xof2,yof2 in zip((p['x']-1,p['x'],p['x']+1,p['x']),(p['y'],p['y']-1,p['y'],p['y']+1)):						
							if not(xof2 == p['lx'] and yof2 == p['ly'] or ( xof2 < 0 or xof2 >= len(maze[0]) or yof2 < 0 or yof2 >= len(maze) ) ) :
								if maze[yof2][xof2] == '>' or maze[yof2][xof2] == '<' or maze[yof2][xof2] == '^' or maze[yof2][xof2] == 'v':
									pos.append( {'x':xof2 + slopes[maze[yof2][xof2]]['x'],'y':yof2 + slopes[maze[yof2][xof2]]['y'],'lx':xof2,'ly':yof2,'s':p['s']+2,'start':{'x':xof2+1,'y':yof+1},'end':False }  )	
				if deadEnd:
					p['s'] = 0
					p['end'] = True

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 94,"Test failed, expected 94, result "+str(test_value)
	print(main("INPUT"))
