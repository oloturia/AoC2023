#!/usr/bin/python3

def main(input_file):
	rules = dict()
	materials = list()
	with open(input_file) as f:
		rule_parser = True
		for read_line in f.readlines():
			if rule_parser:
				if len(read_line) > 1:
					rules[read_line.split("{")[0]] =  read_line.split("{")[1][:-2].split(',')	
				else:
					rule_parser = False
			else:
				materials.append(read_line)
				
	accepted = 0	
	for mat in materials:
		r = 'in'
		i = 0
		x = int(mat[1:-2].replace('=',',').split(',')[1])
		m = int(mat[1:-2].replace('=',',').split(',')[3])
		a = int(mat[1:-2].replace('=',',').split(',')[5])
		s = int(mat[1:-2].replace('=',',').split(',')[7])
		while not (r == 'A' or r == 'R'):
			if not('<' in rules[r][i].split(':')[0] or '>' in rules[r][i].split(':')[0]):
				r = rules[r][i]
				i = 0
			elif eval(rules[r][i].split(':')[0]):
				r = rules[r][i].split(':')[1]
				i = 0
			else:
				i += 1
			if r == 'A':
				accepted += (x+m+a+s)
	return accepted

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 19114,"Test failed, expected 19114, result "+str(test_value)
	print(main("INPUT"))
