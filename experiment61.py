import sys
input1 = sys.stdin.read()

def comp(nuc):
    nucleotides = 'ATCGN'
    complements = 'TAGCN'
    i = nucleotides.find(nuc)
    comp1 = complements[i]
    return comp1

def revcomp(seq):
    seq = seq.upper()
    seq2 = ''
    for nuc in seq:
	    seq2 = comp(nuc) + seq2
    return seq2

print('The forward and reverse primers are:', input1)
print('The reverse complement of input sequences:', revcomp(input1))
