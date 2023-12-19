#!/usr/bin/python3
from dijkstar import Graph, find_path

input_lines = list()
directions = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}

def main(input_file):
	global input_lines
	global directions
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	nodes = dict()
	graph = Graph()
	
	graph.add_edge('S',(0,0,1),0)
	graph.add_edge('S',(0,0,2),0)
	
	for row,line in enumerate(input_lines):
		for col,char in enumerate(line):
			for d in directions:
				weight = 0
				for i in range(1,4):
					xnext = row + directions[d][0]*i
					ynext = col + directions[d][1]*i
					
					if xnext >= len(input_lines[0]) or xnext < 0 or ynext >= len(input_lines) or ynext < 0:
						break
					elif xnext == len(input_lines[0])-1 and ynext == len(input_lines)-1:
						graph.add_edge((row,col,d),'E',weight)
						break
					else:
						weight += int(input_lines[xnext][ynext])
						graph.add_edge((row,col,d),(xnext,ynext,(d+1)%4),weight)
						graph.add_edge((row,col,d),(xnext,ynext,(d-1)%4),weight)

	shortest_path = find_path(graph, 'S','E')	
	return shortest_path.total_cost + int(input_lines[len(input_lines[0])-1][len(input_lines)-1])
	
if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 102,"Test failed, expected 102, result "+str(test_value)
	print(main("INPUT"))
