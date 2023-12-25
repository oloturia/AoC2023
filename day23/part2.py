#!/usr/bin/python3
nodes = dict()
maze = list()
arrival = tuple()
result = 0

def deepsearch(node,visited):
	global nodes
	global result
	global arrival
	
	for n in nodes[node]:
		if n[0] == arrival:
			visited.append(arrival)
			steps = 0		
			for i,start in enumerate(visited[:-1]):
				for end in nodes[start]:
					if end[0] == visited[i+1]:
						steps += end[1]
			steps -= 1
			result = steps if steps > result else result
			return
		if n[0] in visited:
			continue
		else:			
			local_visited = visited.copy()
			local_visited.append(n[0])
			deepsearch(n[0],local_visited)
	return

class PathFinder:
	def __init__(self,pos,direction):
		self.pos = pos
		self.startpos = direction
		self.direction = direction
		self.steps = 0
		self.active = True
	
	def move(self):
		global nodes
		global maze
		global arrival
		if self.active:
			exits = tuple()
			for xof,yof in zip((self.pos[0]-1,self.pos[0],self.pos[0]+1,self.pos[0]),(self.pos[1],self.pos[1]-1,self.pos[1],self.pos[1]+1)):
				if not(( (xof,yof) == self.direction  ) or ( xof < 0 or xof >= len(maze[0]) or yof < 0 or yof >= len(maze) ) ) and maze[yof][xof] != '#':
					exits = (xof,yof)
					
			if exits == tuple():
				self.active = False
			elif exits in nodes:
				self.steps += 2
				nodes[self.startpos].append([exits,self.steps])
				self.active = False
			else:
				self.direction = self.pos
				self.pos = exits
				self.steps += 1
				if self.pos == arrival:
					nodes[self.startpos].append([self.pos,self.steps])
					self.active = False
					
		return self.active
			
def main(input_file):
	global nodes
	global maze
	global arrival
	global result
	maze.clear()
	nodes.clear()
	result = 0
	
	with open(input_file) as f:
		maze = [line.rstrip() for line in f.readlines()]	
	arrival	= (len(maze[0])-2,len(maze)-1)
	nodes = dict()
	
	for y,row in enumerate(maze):
		for x,col in enumerate(row):
			if y == len(maze)-1:
				break
			countslopes = 0
			if col == '.':
				for xi,yi in zip((0,-1,0,1),(1,0,-1,0)):
					if maze[y+yi][x+xi] in ("<^>v"):
						countslopes += 1
				if countslopes > 1:
					nodes[(x,y)] = list()
					
	
	nodes[(0,1)] = list()

	for node in nodes:
		curpos = node
		exits = list()
		for xi,yi in zip((0,-1,0,1),(1,0,-1,0)):
			if maze[curpos[1]+yi][curpos[0]+xi] in ("<^>v"):
				exits.append((curpos[0]+xi,curpos[1]+yi))
			if node == (0,1):
				exits = [(0,0)]
		PathFinders = list()
		for ex in exits:
			PathFinders.append(PathFinder(ex,curpos))
		finding = True
		while finding:
			finding = False
			for pathfinder in PathFinders:
				found = pathfinder.move()
				if found:
					finding = True

	treetop = (0,1)
	deepsearch(treetop,[treetop])
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 154,"Test failed, expected 154, result "+str(test_value)
	print(main("INPUT"))
