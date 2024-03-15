from DNASeq import *
from codon_table import *
import sys

if len(sys.argv) < 3:
    print("Input codon table and DNA sequence on command-line.")
    sys.exit(1)

codonfile = sys.argv[1]
ct = codon_table(codonfile)

table = ct.codontable(codonfile)

seq = sys.argv[2]
ds = DNASeq(seq)
seq = ds.seq

print('===original sequence===\n', 'There are', ds.freq(seq) ,'in the sequence\n', 'Number of potential start codons:', ds.atg(seq), '\n', ds.seq, '\n\n', '===comp sequence===\n', ds.comp(seq), '\n\n', '\n===reverse comp===\n', ds.revComp(seq), '\n')


print('Forward frame 1:', ds.trans(seq, table, 1))
print('Forward frame 2:', ds.trans(seq, table, 2))
print('Forward frame 3:', ds.trans(seq, table, 3))

rev = ds.revComp(seq)

print('Rev forward frame 1:', ds.trans(rev, table, 1))
print('Rev forward frame 2:', ds.trans(rev, table, 2))
print('Rev forward frame 3:', ds.trans(rev, table, 3))



