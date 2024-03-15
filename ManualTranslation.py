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

#adding more keys and values to the codon table
ambiguous = {}
ambiguousbad = {}
for n1 in 'TCAG':
	for n3 in 'ATCG':
		for n2 in 'ATCG':
			codon = n1 + n2 + n3
			if codons[n1+n2+'A'] == codons[codon] and codons[n1+n2+'T'] == codons[codon] and codons[n1+n2+'C'] == codons[codon] and codons[n1+n2+'G'] == codons[codon]:
				ambcodons = n1 + n2 + 'N'
				ambiguous[ambcodons] = codons[codon]
				codons.update(ambiguous)
			else:
				ambcodon = n1 + n2 +'N'
				ambcodon2 = 'N' + n2 + n3
				ambcodon3 = n1 + 'N' + n3
				ambiguousbad[ambcodon] = 'X'
				ambiguousbad[ambcodon2] = 'X'
				ambiguousbad[ambcodon3] = 'X'
				codons.update(ambiguousbad)
#reading frames 1-3:

seq = ''.join(seq1.read().split())
seqlen = len(seq)
aaseq = []
aa2seq = []
aa3seq = []
def transl(x):
	for x in range(0,seqlen,3):
		codon = seq[x:x+3]
		codon2 = seq[x+1:x+4]
		codon3 = seq[x+2:x+5]
		
			
		if len(codon) and len(codon2) and len(codon3) == 3: 
			aa1 = codons[codon]
			aaseq.append(aa1)
			aa2 = codons[codon2]
			aa3 = codons[codon3]
			aa2seq.append(aa2)
			aa3seq.append(aa3)
		else:
			break
			
	return ''.join(aaseq),''.join(aa2seq),''.join(aa3seq)
	

print('The first, second and third reading frames:', transl(x))


#reverse complement

def reversecomp(seq):
	seq = seq.upper()
	seq = seq.replace('A', 't')
	seq = seq.replace('T', 'a')
	seq = seq.replace('C', 'g')
	seq = seq.replace('G','c')
	seq = seq.upper()
	return ''.join(reversed(seq))

#reverse complement reading frames 1-3
revcomp = reversecomp(seq)
revcodon = []
revcodon2 = []
revcodon3 = []
def translrev(seq):
	for i in range(0,len(revcomp),3):
		codonrev = revcomp[i:i+3]
		codonrev2 = revcomp[i+1:i+4]
		codonrev3 = revcomp[i+2:i+5]
		if len(codonrev) and len(codonrev2) and len(codonrev3) == 3:
			aarev = codons[codonrev]
			revcodon.append(aarev)
			aarev2 = codons[codonrev2]
			revcodon2.append(aarev2)
			aarev3 = codons[codonrev3]
			revcodon3.append(aarev3)
		else:
			break
	return ''.join(revcodon),''.join(revcodon2),''.join(revcodon3)

print('The 3 reading frames for the reverse complement strand:', translrev(revcomp))


