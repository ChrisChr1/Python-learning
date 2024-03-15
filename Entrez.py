from Bio import Entrez

Entrez.email = 'cm2055@georgetown.edu'

handle = Entrez.esearch(db='protein', term = 'Homo sapiens[orgn] AND BRCA2[Gene] AND REFSEQ', retmode= "fasta", idtype= 'acc')
record = Entrez.read(handle)

ids = record['IdList']


with open("BRCA2gene.fas", "w") as file1:
	for id in ids:
		fasta_records = Entrez.efetch(db="protein", id = id, rettype = "fasta", retmode="text", idtype = "acc")
		record2 = fasta_records.read()
		file1.write(record2)





    



