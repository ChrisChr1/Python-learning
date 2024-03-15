#Input
SASP = 'TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'

#SASP = 'N GCGCGCGCATGTTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'

#SASP = 'ATGTTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG'


#Finding start codon and translation frame
if SASP.startswith('ATG'):
	print('There is a start codon in the beginning of SASP')
else:
	print('There is no start codon in the beginning of SASP')

metcodon = SASP.find('ATG')

translation_frame = (metcodon % 3) +1

#counting total nucleic acids
countnucs = SASP.count('')+1

#Counting amino acids
trunkSASP = SASP[21:]
counttrunk = trunkSASP.count('')
aminoacids = counttrunk//3

#GC Content
Gcont = SASP.count('G')
Ccont = SASP.count('C')
GCcont = (Gcont+Ccont)/len(SASP)*100

#Output
print('The start codon is at position', metcodon)
print('The reading frame is', translation_frame)
print('There are', countnucs, 'nucleic acids')
print('There are', aminoacids, 'amino acids')
print('The SASP sequence has', round(GCcont), 'percent GC content')






