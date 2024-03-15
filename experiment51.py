#Forward and reverse primer program


primer1 = 'GCAGCCTTTGTGAACCAACAC'
primer2 = 'CCCCGCACACTAGGTAGAGA'
primer3 = 'cccccctttnnnacac'

def complement(primer):
    nucs = 'ATCGN'
    comps = 'TAGCN'
    i=nucs.find(primer)
    if i >= 0:
        comp = comps[i]
    else:
        comp = primer
    return comp


def revcomp(primer):
    seq = primer.upper()
    seq2 = ''
    for primer in seq:
        seq2 = complement(primer) + seq2
    return seq2

print('The reverse complement sequence of', primer1 ,'is: ', revcomp(primer1))
print('The reverse complement sequence of', primer2 ,'is: ', revcomp(primer2))

