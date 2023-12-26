#!/usr/bin/python3
from sympy.solvers import solve
from sympy import symbols, Symbol, Eq

def main(input_file):
	k = list()
	kd = list()
	with open(input_file) as f:
		lines = f.readlines()
		for i1 in range(3):
			line = lines[i1]
			k.append(list())
			kd.append(list())
			for i2 in range(3):
				k[i1].append( int(line.rstrip().split('@')[0].split(',')[i2]) )
				kd[i1].append( int(line.rstrip().split('@')[1].split(',')[i2]) )

	u = symbols('x, y, z')
	tu = symbols('t1, t2, t3')
	dtu = symbols('dt1, dt2, dt3')
	equations = list()	

	for i1 in range(3):
		for i2 in range(3):
			equations.append(Eq(k[i1][i2] + kd[i1][i2] * tu[i1] - ( dtu[i2] * tu[i1] ), u[i2]))
	
	result = solve(equations,u+tu+dtu,dict=True )[0]
	return result[u[0]]+result[u[1]]+result[u[2]]

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 47,"Test failed, expected 47, result "+str(test_value)
	print(main("INPUT"))
