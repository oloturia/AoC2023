#!/usr/bin/python3

def main(input_file):
	seeds_to_soil = list()
	remapped = list()
	with open(input_file) as f:
		for line in f.readlines():
			line = line.rstrip()
			maps = tuple()
			if line[0:6] == "seeds:":
				seeds_to_soil = [int(x) for x in line[7:].split()]
				remapped = seeds_to_soil.copy()
			elif ":" in line:
				seeds_to_soil = remapped.copy()
			elif line != "":
				maps = tuple(int(x) for x in line.split())
				for i,el in enumerate(seeds_to_soil):
					if el in range(maps[1],maps[1]+maps[2]):
						remapped[i] = maps[0] + (el-maps[1])
	return min(remapped)

if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 35,"Test failed, expected 35, result "+str(test_value)
	print(main("INPUT"))
