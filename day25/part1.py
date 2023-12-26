#!/usr/bin/python3
import networkx as nx

def main(input_file):
	linked_to = dict()
	with open(input_file) as f:
		for line in f.readlines():
			linked_to[line.split(':')[0]] = line.rstrip().split(':')[1].split()
	
	G = nx.Graph()
	for top,linked in linked_to.items():
		for link in linked:
			G.add_edge(top,link,capacity=1.0)

	path=nx.all_pairs_shortest_path_length(G)
	maxdist = 0
	for n1 in path:
		for n2,dst in n1[1].items():
			if dst > maxdist:
				source = n1[0]
				sink = n2
				maxdist = dst
			
	a,s = nx.minimum_cut(G,source,sink)
	return len(s[0])*len(s[1])

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 54,"Test failed, expected 54, result "+str(test_value)
	print(main("INPUT"))
