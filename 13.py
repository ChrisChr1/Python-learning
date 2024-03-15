import pysam

bf = pysam.Samfile('10_Normal_Chr21.bam')


for pileup in bf.pileup('21'):
	counts = {}
	cover =[]
	for pileupread in pileup.pileups:
		if pileupread.indel:
			continue
		if pileupread.is_del:
			continue
		al = pileupread.alignment
		if al.is_unmapped:
			continue
		if al.is_secondary:
			continue
		if int(al.opt('NM')) >1:
			continue
		if int(al.opt('NH')) >1:
			continue
		if not pileupread.query_position:
			continue
		readbase=pileupread.alignment.seq[pileupread.query_position]
		if readbase not in counts:
			counts[readbase] = 0
		counts[readbase] += 1
	
	#filtering out homozygosity
	if len(counts)<2:
		continue
	#filtering out for true heterozygosity
	if sorted(counts.values())[-1] // sorted(counts.values())[-2] > 1 or sorted(counts.values())[-2] // sorted(counts.values())[-1] > 1 or sorted(counts.values())[-1] // sorted(counts.values())[0] > 1 or sorted(counts.values())[0] // sorted(counts.values())[-1] > 1:
		continue
	#Attempt
	#cover.append(pileup.n)
	#covermax = sorted(cover)
	#print(covermax[-1])

	#finding max coverage
	if pileup.n > 740:
		print(pileup.pos, pileup.n, end= ' ')
		for base in sorted(counts):
			print(base, counts[base], end=" ")
		print()
bf.close()
