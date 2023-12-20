#!/usr/bin/python3
rules = dict()
result = 0

def exploreTree(node,limits):
	global rules
	global result

	if node == 'A':
		temp = (limits['xt'] - limits['xl']+1) * (limits['mt'] - limits['ml']+1) * (limits['at'] - limits['al']+1) * (limits['st'] - limits['sl']+1)
		result += temp
		return
	if node == 'R':
		return 
	
	for r in rules[node]:
		if '<' in r:
			quota = int(r.split('<')[1].split(':')[0])
			new_limits = limits.copy()
			if new_limits[r[0]+'t'] > quota:
				new_limits[r[0]+'t'] = quota - 1
			exploreTree(r.split(':')[1],new_limits)
			if limits[r[0]+'l'] <= quota:
				limits[r[0]+'l'] = quota
				
		elif '>' in r:
			quota = int(r.split('>')[1].split(':')[0])
			new_limits = limits.copy()
			if new_limits[r[0]+'l'] < quota:
				new_limits[r[0]+'l'] = quota + 1
			exploreTree(r.split(':')[1],new_limits)
			if limits[r[0]+'t'] >= quota:
				limits[r[0]+'t'] = quota 		
		else:
			exploreTree(r,limits)
	return

def main(input_file):
	global rules
	global result
	
	result = 0
	rules.clear()
	
	with open(input_file) as f:
		for read_line in f.readlines():
			if len(read_line) > 1:
				rules[read_line.split("{")[0]] = read_line.split("{")[1][:-2].split(',')
			else:
				break
				
	path = dict()
	exploreTree('in',{'xl':1,'xt':4000,'ml':1,'mt':4000,'al':1,'at':4000,'sl':1,'st':4000})
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 167409079868000,"Test failed, expected 167409079868000, result "+str(test_value)
	print(main("INPUT"))
