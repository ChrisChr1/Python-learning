import sys
input1 = sys.argv[1]

inputprimers = open(input1).read()

pp1 = ''.join(inputprimers.split()[0:2])

pp2 = ''.join(inputprimers.split()[4:6])
	
pp3 = ''.join(inputprimers.split()[8:10])


def comp(nuc):
	nucs = 'ACGTacgtNn'
	comps = 'TGCAtgcaNn'
	i = nucs.find(nuc)
	if i >= 0:
		return comps[i]
	return nuc

def reverse_comp(primer):
	rev = ""
	for n in primer:
		rev = comp(n) + rev
	return rev
print('The reverse complement of the first primer pairs are:', reverse_comp(pp1))
print('The reverse complement of the first primer pairs are:', reverse_comp(pp2))
print('The reverse complement of the first primer pairs are:', reverse_comp(pp3))

