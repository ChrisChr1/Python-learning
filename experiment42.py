#HW2.2

#Input sequences

#seq = 'AAAAAAAAAAAAAAAA'

#seq = 'CACACACACACACACA'

#seq = 'ATTCGATTCGATTCG'

seq = 'GTAGTAGTAGTAGTA'

#seq = 'TCAGTCACTCACTCAG'

#seq = 'AGANNNAGA'

#seq = 'jfjfjfjf'

#seq = 'AaaaAAAaaa'

#seq = 'tgcggcggcggcgt'



# For loop
		
for i in range(1, len(seq)+1):
#	print(i)
	newseq = seq[0:i]
#	print(newseq)

	if newseq*2 == seq:
		print ('This sequence has two tandem repeats')

	elif newseq*3 == seq:
		print ('This sequence has three tandem repeats')

	elif newseq*4 == seq:
		print('This sequence has four tandem repeats')

	elif newseq*5 == seq:
		print ('This sequence has five tandem repeats')

	elif newseq*6 == seq:
		print ('This sequence has six tandem repeats')

	elif newseq*7 == seq:
		print ('This sequence has seven tandem repeats')

	elif newseq*8 == seq:
		print ('This sequence has eight tandem repeats')

	elif newseq*16 == seq:
		print('This sequence has sixteen tandem repeats')

	else:
		0

