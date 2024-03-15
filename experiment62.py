import sys
seq1 = 'GCAGCCTTTGTGAACCAACAC'
seq2 = 'CCCCGCACACTAGGTAGAGA'
input1 = sys.argv[1]


def comp(nuc):
	nucleotides = 'ATCGN'
	complements = 'TAGCN'
	i = nucleotides.find(nuc)
	comp1 = complements[i]
	return comp1


def rev(seq):
	seq = seq.upper()
	seq1 = ''
	for nuc in seq:
		seq1 = nuc + seq1
	return seq1

def compall(seq):
	seq = seq.upper()
	seq1 = ''
	for nuc in seq:
		seq1 = seq1 + comp(nuc)
	return seq1

def revcomp(seq):
	seq = seq.upper()
	seqrev = ''
	for nuc in seq:
		seqrev = comp(nuc) + seqrev
	return seqrev

if input1 == 'Complement':
	print(compall(seq1))
	print(compall(seq2))

elif input1 == 'Reverse':
	print(rev(seq1))
	print(rev(seq2))

elif input1 == 'Reversecomplement':
	print(revcomp(seq1))
	print(revcomp(seq2))
else:
	print('Wrong input. Try typing Complement, Reverse or Reversecomplement')


    


