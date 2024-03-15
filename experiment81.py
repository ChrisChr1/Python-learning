#first program

#input1 = 'cacacacgggg'
input1 = 'nnNNATGatgatg'
#input1 = 'rnatatatatatatatatattttttttttttttttttt'

def comp(seq):
    comps = {'N':'N', 'A':'T', 'C':'G','T':'A','G':'C',}
    sequence = list(seq)
    sequence = [comps[nuc] for nuc in sequence]
    return ''.join(sequence)

def rev(seq):
    seq = seq.upper()
    seq1 = ''
    for nuc in seq:
        seq1 = comp(nuc) + seq1
    return seq1

print('This is the first program output:', rev(input1))


#second program

comps = {'n':'N','N':'N','a':'T', 'A':'T', 'c':'G', 'C':'G', 't':'A', 'T':'A','G':'C', 'g':'C'}

revcomp = ''.join(comps.get(nuc, comp) for nuc in reversed(input1))

print('Second program for the reverse complement: ', revcomp)

#third program

def reversecomp(seq):

    comps = {'n':'N','N':'N','a':'T', 'A':'T', 'c':'G', 'C':'G', 't':'A', 'T':'A','G':'C', 'g':'C'}

    return ''.join(reversed([comps[nuc] for nuc in seq]))
                   
print('Third program for reverse complement:', reversecomp(input1))

    
