#!/usr/bin/python3
import math

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
					if 'rx' in line:
						target = line.split(" -> ")[0][1:]
	
	periods = dict()
	for line in input_lines:
		if input_lines[line]['t'] == '&':
			for keys,values in input_lines.items():
				for v in values['a']:
					if v == line:
						input_lines[line]['s'][keys] = False
						if line == target:
							periods[keys] = 0
	i = 0
	found = True
	while found:
		i += 1
		elab = [{'a':"broadcaster",'s':False,'f':''}]
		a = 0
		while len(elab) > 0:	
			throws = list()
			for e in elab:
				if e['a'] == 'rx':
					continue
				if input_lines[e['a']]['t'] == '%' and not e['s']:
					input_lines[e['a']]['s'] = not input_lines[e['a']]['s']
					throws.append( (e['a']) )
				elif input_lines[e['a']]['t'] == '&':
					input_lines[e['a']]['s'][e['f']] = e['s']
					throws.append( (e['a']) )
				elif e['a'] == "broadcaster":
					throws.append("broadcaster")
			elab = list()
			for tr in throws:
				if input_lines[tr]['t'] == '%':
					for node in input_lines[tr]['a']:
						elab.append({'a':node,'s':not input_lines[tr]['s'], 'f':tr})
				elif input_lines[tr]['t'] == '&':
					for node in input_lines[tr]['a']:
						if False in input_lines[tr]['s'].values():
							elab.append({'a':node,'s':True,'f':tr})
						else:
							elab.append({'a':node,'s':False,'f':tr})
				elif tr == "broadcaster":
					for node in input_lines["broadcaster"]['a']:
						elab.append({'a':node,'s':False,'f':"broadcaster"})
			found = False
			for per in periods:
				if input_lines[target]['s'][per] and periods[per] == 0:
					periods[per] = i-1
				if periods[per] == 0:
					found = True
			if not found:
				break
					
	lcm = 0
	for per in periods:
		if lcm == 0:
			lcm = periods[per]
			continue
		lcm = lcm*periods[per]//math.gcd(lcm,periods[per])
	return lcm
	
if __name__ == "__main__":
	print(main("INPUT"))
