#seq = 'TTGAGTAGACGCGTCTACTCAA'

seq = 'TTGAGTAGACGTCGTCTACTCAA'

#seq = 'ATATATATATATATAT'

#seq = 'ATCTATATATATGTAT'

#seq = 'AGTACT'

#seq = 'agagagactct'

#seq = 'agtact'


def comp(nuc):
	nucleotides = 'ATCG'
	complements = 'TAGC'
	i = nucleotides.find(nuc)
	if i >= 0:
		comp = complements[i]
	else:
		comp = ''

	return comp

def revcomp(seq):
	seq2 = ''
	for nuc in seq:
		seq2 = comp(nuc)+ seq2
	return seq2

def palindrome(seq):
	seq = (seq).upper()
	firsthalf = seq[0:len(seq)//2]
	lasthalf_even = seq[len(seq)//2:]
	lasthalf_odd = seq[len(seq)//2+1:]
	if len(seq)%2 == 0 and firsthalf == revcomp(lasthalf_even):
		print('This is a reverse complement palindrome')
	elif len(seq)%2 > 0 and firsthalf == revcomp(lasthalf_odd):
		print('This is a reverse compliment palindrome')
	else:
		print('This is not a reverse compliment palindrome')

(palindrome(seq))
