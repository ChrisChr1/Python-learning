import sys
translation_file = sys.argv[1]
transl = open(translation_file)
seq_file = sys.argv[2]
seq1 = open(seq_file)

data = {}
for items in transl:
	s = items.split()
	key = s[0]
	value = s[2]
	data[key] = value
transl.close()
	
b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons={}
init = {}
n = len(aa)
for x in range(n):
	codon = b1[x]+b2[x]+b3[x]
	codons[codon] = aa[x]
	init[codon] = (st[x] == 'M')

seq = ''.join(seq1.read().split())
seqlen = len(seq)
aaseq = []

for x in range(0,seqlen,3):
	codon = seq[x:x+3]
	aa = codons[codon]
	aaseq.append(aa)
print(''.join(aaseq))

for i in range(0,seqlen,3):
	codon = seq[i:i+3]
	aa = codons[codon]
	aaseq.append(aa)
	if init[codon] == True:
		print('Correct codon table: The SASP gene begins with a start codon')
	else:
		print('Wrong codon table')
	break
seq1.close()
