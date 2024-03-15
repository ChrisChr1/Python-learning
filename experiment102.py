#Write a program to compute and output the frequency of each nucleotide in a
#DNA sequence using a dictionary (see lec. 9).

#Output the frequencies in most-occurrences to least-occurrences order

import sys
input1 = sys.argv[1]
seq = ''.join(open(input1).read().split())


seq = seq.upper()
freq = {}
for n in seq:
	freq[n] = freq.get(n, 0) + 1

seqlist = [(n,t) for n,t in freq.items()]

seqlist.sort(key = lambda a:a[1])

print(seqlist[::-1])
