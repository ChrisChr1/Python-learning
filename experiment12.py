import Bio.SeqIO
import gzip

handle1 = gzip.open("human.protein.fasta.gz", mode="rt")		
count = {}
countall1 = 0
for record in Bio.SeqIO.parse(handle1, "fasta"):
	for aa in record.seq:
		countall1 += 1
		count[aa] = count.get(aa,0)+1
		maxi = max(count, key=count.get)
		percentmaxi = (count[maxi]/countall1)*100
		mini = min(count,key = count.get)
		percentmini = (count[mini]/countall1)*100

print('RefSeq:')
print(maxi,'=', percentmaxi,'%')
print(mini, '=', percentmini,'%')


handle2 = gzip.open("uniprot_sprot_human.xml.gz", mode="rt")
count2 = {}
countall = 0
for record in Bio.SeqIO.parse(handle2, "uniprot-xml"):
	for aa in record.seq:
		countall += 1
		count2[aa] = count2.get(aa,0)+1
		maxi = max(count2, key=count2.get)
		percentmaxi = (count2[maxi]/countall)*100
		mini = min(count2, key=count2.get)
		percentmini = (count2[mini]/countall)*100

print('Uniprot proteome:') 
print(maxi,'=', percentmaxi,'%')
print(mini, '=', percentmini,'%')

differ = {x:count[x]-count2[x] for x in count if x in count2}
maxdif = sorted(differ.items(), key=lambda x:x[1], reverse=True)
print('The top 5 differences between each amino acid in the files', maxdif[0:5])



	


