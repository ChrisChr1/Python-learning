#HW2 from starting HW1 solution
codon1 = 'ATG'
codon2 = codon1.lower()
codon3 = 'AcG'
codon4 = 'gTc'


first = codon1[0]
second = codon1[1]
third = codon1[2]

reverse1 = third+second+first

lowercase1 = reverse1.lower()

#complement function
def complement(nuc):
	comp = ''
	if nuc == 'a':
		comp = 't'
	elif nuc == 'c':
		comp = 'g'
	elif nuc == 'g':
		comp = 'c'
	elif nuc == 't':
		comp = 'a'
	elif nuc == 'A':
		comp = 't'
	elif nuc == 'C':
		comp = 'g'
	elif nuc == 'G':
		comp = 'c'
	elif nuc == 'T':
		comp = 'a'
	else:
		comp = nuc
	return comp

#making a string from complement()
def full_complement(codon):
	string = ''
	for na in codon:
		x = complement(na)
		string = string+x
	return string

#reverse function
def reverse(string):
	first=string[0]
	second=string[1]
	third=string[2]
	reverse = third+second+first	
	return reverse

#output
print('The complement of ATG is', reverse(full_complement('ATG')))
print('The complement of cccc is', reverse(full_complement('cccc')))
print('The complement of NNg is', reverse(full_complement('NNg')))
