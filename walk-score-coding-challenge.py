import sys
nodes = { } # nodes will be a dictionary of node : list of sucessors
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

#Time to sit down and think about this.  Two goals:
# 1) traverse all the nodes, figure out which ones need to be cut
# 2) perform the cuts by dropping the cut ones and relinking the remaining nodes
# easy to do in two loops, but want to minimize number of operations.  since we
# need to loop to read the nodes in anyways, that's a good place to identify
# ones that will need to be cut.  a second recursive function to do the cutting
# and re-linking shouldn't be too difficult if all the data is already in place
