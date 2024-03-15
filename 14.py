import xml.etree.ElementTree as ET
import urllib.request


#The original file that I chose
file1 = urllib.request.urlopen('https://rest.uniprot.org/uniprotkb/P09848.xml')

#The file to check for bugs in the code
#file1 = urllib.request.urlopen('https://rest.uniprot.org/uniprotkb/P05067.xml')

doc = ET.parse(file1)
ns = '{http://uniprot.org/uniprot}'

root= doc.getroot()
enter = root.find(ns+'entry')
ref = enter.findall(ns+'reference')

print('\x1B[1m'+'\n\n======= Bibliography =======\n\n'+ '\x1B[0m')

for ele in ref:
	cite = ele.find(ns+'citation')

	#If title in cite exists/ if title does not exist
	if cite.find(ns+'title') in cite:
		title = cite.find(ns+'title')
		titles = title.text
	else:
		titles = ''
	
	pubmed = cite.find(ns+'dbReference')
	authors = cite.find(ns+'authorList')
	#Find names in attribute and print value from name key
	for ele in authors:
		names = ele.attrib
		print(names['name'], end =', ')

	print(titles, cite.attrib['name'],cite.attrib['date']+';'+cite.attrib['volume']+':'+cite.attrib['first']+'-'+cite.attrib['last']+'.', end = ' ')

	#A for loop excluding DOI print out if no DOI in reference
	for doi in cite.findall(ns+'dbReference'):
		dbref = doi.attrib
	if dbref['type'] == 'DOI':
		type1 = dbref['type']
		id1 = dbref['id']
		print(type1+':'+id1+'.', pubmed.attrib['type']+':'+pubmed.attrib['id']+'.', end= '\n\n')
	else:
		print(pubmed.attrib['type']+':'+pubmed.attrib['id']+'.', end= '\n\n')

file1.close()

