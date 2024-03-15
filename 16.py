from MyDNAStuffmodule import *
import sys

try:
	codonfile = sys.argv[1]
	codons, init = codontable(codonfile)
except IndexError:
	print('Input codon table into command-line. Type codon table file first followed by sequence file.')
	sys.exit(1)
except IOError:
	print('Unable to locate codon table file. Check spelling and try again.')
	sys.exit(1)

try:
	seqfile = sys.argv[2]
	seq = readseq(seqfile)
except IndexError:
	print('Input DNA sequence file into command-line.')
	sys.exit(1)
except IOError:
	print('Unable to locate DNA sequence file. Check spelling and try again.')
	sys.exit(1)


print('The sequence is:', seq, end='\n\n')
print('The complement of this sequence is:', comp(seq),end ='\n\n')
print('The reverse complement of this sequence is:', revComp(seq),end ='\n\n')

for frame in (1,2,3):
	print("Forward frame", frame, ':', trans(codons, seq, frame, init),end='\n\n')



for frame in (1,2,3):
	print("Reverse frame",frame,':', trans(codons, revComp(seq), frame, init),end='\n\n')


freq(seq)

atg(seq)
