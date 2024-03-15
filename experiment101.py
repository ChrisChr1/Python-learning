import sys
input1 = sys.argv[1]
seq = ''.join(open(input1).read().split())


def reversecomp(seq):
	compdict = {'n':'N','N':'N','a':'T', 'A':'T', 'c':'G', 'C':'G', 't':'A', 'T':'A','G':'C', 'g':'C'}
	revcomp = ''.join(compdict.get(n, compdict) for n in reversed(seq))
	return revcomp

print(reversecomp(seq))
