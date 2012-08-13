import sys
nodes = { }
for line in sys.stdin.readlines():
	arc = line.split()
	if len(arc) == 2:
		head, tail = arc[0], arc[1]
		if head in nodes:
			nodes[head].append(tail)
		else:
			nodes[head] = [ tail ]
	else:
		print('Invalid edge definition, not included: {}'.format(line))
for head in nodes:
	for tail in nodes[head]:
		print(head + '\t' + tail)