#!/usr/bin/python3

def main(input_file):
	seeds_to_soil = list()
	remapped = list()
	with open(input_file) as f:
		for line in f.readlines():
			line = line.rstrip()
			if line[0:6] == "seeds:":
				for x,val in enumerate(line[7:].split()):
					if x%2 == 0:
						seeds_to_soil.append( [ int(val),int(val) + int(line[7:].split()[x+1]) -1] )
			elif ":" in line:
				for el in seeds_to_soil:
					remapped.append(el)
				seeds_to_soil = remapped.copy()
				remapped = list()
			elif line != "":
				start_source = int(line.split()[1])
				stop_source = int(line.split()[1]) + int(line.split()[2]) -1
				start_dest = int(line.split()[0])
				stop_dest = int(line.split()[0]) + int(line.split()[2]) -1
				i = 0
				while i < len(seeds_to_soil):
					start_sds = seeds_to_soil[i][0]
					stop_sds = seeds_to_soil[i][1]
					if start_sds >= start_source and stop_sds <= stop_source:
						remapped.append([start_dest + (start_sds-start_source), start_dest + (start_sds-start_source) + (stop_sds-start_sds)] )
						seeds_to_soil.pop(i)
						continue
					elif start_sds < start_source and stop_sds >= start_source and stop_sds <= stop_source:
						remapped.append( [start_dest, start_dest + (start_sds-start_source) + (stop_sds-start_sds) ] ) 
						seeds_to_soil[i] = [start_sds, start_source -1] 
					elif start_sds >= start_source and start_sds <= stop_source and stop_sds > stop_source:
						remapped.append( [start_dest+(start_sds-start_source) ,stop_dest] )
						seeds_to_soil[i] = [stop_source +1,stop_sds]
					i += 1

	for el in seeds_to_soil:
		remapped.append(el)
	seeds_to_soil = remapped.copy()
	
	result = seeds_to_soil[0][0]
	for i in seeds_to_soil:
		if result > i[0]:
			result = i[0]
	return result
	
if __name__ == "__main__":
	test_value = main("TEST")
	assert test_value == 46,"Test failed, expected 46, result "+str(test_value)
	print(main("INPUT"))
