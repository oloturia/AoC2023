#!/usr/bin/python3
import z3

def main(input_file):
	
	hpos = list()
	with open(input_file) as f:
		for line in f.readlines():			
			hpos.append( {'x':int(line.rstrip().split('@')[0].split(',')[0]),'y':int(line.rstrip().split('@')[0].split(',')[1]),'z':int(line.rstrip().split('@')[0].split(',')[2]),'dx':int(line.rstrip().split('@')[1].split(',')[0]),'dy':int(line.rstrip().split('@')[1].split(',')[1]),'dz':int(line.rstrip().split('@')[1].split(',')[2]) } )
	
	sol = z3.Solver()
	x,y,z = z3.Ints('x y z')
	t1,t2,t3 = z3.Ints('t1 t2 t3')
	dt1,dt2,dt3 = z3.Ints("dt1 dt2 dt3")
	
	vect1x = hpos[0]['x'] + hpos[0]['dx']*t1 == x + dt1*t1
	vect1y = hpos[0]['y'] + hpos[0]['dy']*t1 == y + dt2*t1
	vect1z = hpos[0]['z'] + hpos[0]['dz']*t1 == z + dt3*t1

	vect2x = hpos[1]['x'] + hpos[1]['dx']*t2 == x + dt1*t2
	vect2y = hpos[1]['y'] + hpos[1]['dy']*t2 == y + dt2*t2
	vect2z = hpos[1]['z'] + hpos[1]['dz']*t2 == z + dt3*t2

	vect3x = hpos[2]['x'] + hpos[2]['dx']*t3 == x + dt1*t3
	vect3y = hpos[2]['y'] + hpos[2]['dy']*t3 == y + dt2*t3
	vect3z = hpos[2]['z'] + hpos[2]['dz']*t3 == z + dt3*t3

	sol.add(vect1x,vect1y,vect1z,vect2x,vect2y,vect2z,vect3x,vect3y,vect3z)
	sol.check()
	model = sol.model()
	result = model[z].as_long() + model[y].as_long() + model[x].as_long()
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 47,"Test failed, expected 47, result "+str(test_value)
	print(main("INPUT"))
