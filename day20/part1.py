#!/usr/bin/python3

def main(input_file):
	input_lines = dict()
	with open(input_file) as f:
		for line in f.readlines():
			if "broadcaster" in line:
				input_lines["broadcaster"] = {'t':'B','a':line.rstrip().split(" -> ")[1].split(", ")}
			else:
				if line[0] == '%':
					input_lines[line.split(" -> ")[0][1:]] = {'t':'%','a':line.rstrip().split(" -> ")[1].split(", "),'s':False}
				elif line[0] == '&':
					input_lines[line.split(" -> ")[0][1:]] = {'t':'&','a':line.rstrip().split(" -> ")[1].split(", "),'s':dict()}
	
	for line in input_lines:
		if input_lines[line]['t'] == '&':
			for keys,values in input_lines.items():
				for v in values['a']:
					if v == line:
						input_lines[line]['s'][keys] = False
							
	low_signals = 0
	high_signals = 0

	for i in range(1000):
		low = 1
		high = 0
		elab = [{'a':"broadcaster",'s':False,'f':''}]
		while len(elab) > 0:
			new_elab = list()
			for e in elab:
				namen = e['a']
				if namen not in input_lines:
					continue
				typen = input_lines[namen]['t']
				pulsn = e['s']
				fromn = e['f']

				if typen == 'B':	
					for a in input_lines[namen]['a']:
						new_elab.append({'a':a,'s':False,'f':namen})
						low += 1
				elif typen == '%':
					if pulsn == False:
						input_lines[namen]['s'] = not input_lines[namen]['s']
						for a in input_lines[namen]['a']:
							new_elab.append({'a':a,'s':input_lines[namen]['s'],'f':namen})
							if input_lines[namen]['s']:
								high += 1
							else:
								low += 1
				elif typen == '&':
					input_lines[namen]['s'][fromn] = pulsn
					if False in input_lines[namen]['s'].values():
						for a in input_lines[namen]['a']:
							new_elab.append({'a':a, 's':True, 'f':namen })
							high += 1
					else:
						for a in input_lines[namen]['a']:
							new_elab.append({'a':a, 's':False, 'f':namen })
							low += 1			
			elab = new_elab.copy()
			
		low_signals += low
		high_signals += high

	return low_signals * high_signals

if __name__ == "__main__":
	test_value = main("TEST1")
	assert test_value == 32000000,"Test 1 failed, expected 32000000, result "+str(test_value)
	test_value = main("TEST2")
	assert test_value == 11687500,"Test 2 failed, expected 11687500, result "+str(test_value)
	print(main("INPUT"))
