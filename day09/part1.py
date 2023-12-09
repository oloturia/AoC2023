#!/usr/bin/python3

def calc_delta(expr):
	prevel = expr[0]
	new_expr = list()
	for el in expr[1:]:
		new_expr.append( el - prevel )
		prevel = el
	
	return new_expr
		
def main(input_file):
	
	with open(input_file) as f:
		input_lines = [list(map(int,line.rstrip().split())) for line in f.readlines() ]

	result = 0
	for line in input_lines:		
		temp_list = line.copy()
		last_vals = [temp_list[-1]]
		while temp_list != [temp_list[0]]*len(temp_list):		
			temp_list = calc_delta(temp_list)
			last_vals.append( temp_list[-1] )
		result += sum(last_vals)
		
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 114,"Test failed, expected 114, result "+str(test_value)
	print(main("INPUT"))
