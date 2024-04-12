#You should consider scan number 1298 and peptide sequence TYDSYLGDDYVR
#Match against spectra from a given peptide sequence


import xml.etree.ElementTree as ET
import gzip
import sys
from base64 import b64decode
from array import array
import matplotlib.pyplot as plt
import numpy as np 
import warnings

#filter out UserWarning created from stem plots
warnings.filterwarnings(action='ignore', category=UserWarning)

#Check if amount of command-line arguments are correct
if len(sys.argv) < 4:
	print('Input mass spec mzxml.gz file followed by scan number and peptide sequence.')
	exit()
#Check if command-line input is correct
try:
	scan_num = int(sys.argv[2])
except:
	print('Input mass spec mzxml.gz file followed by scan number and peptide sequence.')
	exit()
#check if peptide is valid
try:
	aminoacids = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
	peptide =sys.argv[3]
	if peptide.isdigit() or peptide not in aminoacids:
		raise ValueError
except ValueError:
	print(peptide, 'entered in place of a peptide. Enter a valid peptide instead of numeric entry.')
	exit()

#user input of threshold
threshold = input('Enter a threshold between 0.0012 and 0.4 Da for matching ions in the spectra: ')
try:
	number = float(threshold)
	if not 0.0012 <= number <= 0.4:
		raise ValueError()
except ValueError:
	threshold = 0.2	
	print('Threshold set to 0.20 Da as default.')

#parse through zipfile
zipfilename = sys.argv[1]
zf= gzip.open(zipfilename)
data = ET.parse(zf)
root = data.getroot()
ns = '{http://sashimi.sourceforge.net/schema/}'
scan_num = sys.argv[2]
for scan in root.getiterator(ns+'scan'):
	scanner = scan.attrib
	if scanner['num'] == scan_num:
		peakselt = scan.find(ns+'peaks')
		peaks = array('f',b64decode(peakselt.text))
		if sys.byteorder != 'big':
			peaks.byteswap()
		mzs = peaks[::2] 
		ints = peaks[1::2]

#Find theoretical masses of peptide
peptide = sys.argv[3]
revy = peptide[::-1]
peptide = peptide.upper()
dictmass = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, 
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}
aminoacids = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
sum1 = 0
MZbi =[]

for aa in peptide:
	if aa in aminoacids:
		sum1 = sum1+ dictmass[aa]
		bi = sum1 +1
		MZbi.append(bi)
	
sum2 = 0
MZyi = []
for aa in revy:
	if aa in aminoacids:
		sum2 = sum2 + dictmass[aa]
		yi = sum2 + 19
		MZyi.append(yi)
	#check if amino acid exists			
	

#print('the b ions:', MZbi, 'the y ions:', MZyi)


#Compare the theoretical to experimental and plot
fig, ax = plt.subplots()

listy = []
listb = []
maxi = 0
for mz, intense in zip(mzs, ints):
	#plotting spectrum
	x = np.array([mz])
	y = np.array([intense])
	m,n,baseline = plt.stem(x, y, linefmt='black', use_line_collection=False, markerfmt=' ', basefmt = '', bottom = 0)
	if y > maxi:
		maxi = y
	listmzb=[]
	listmzy = []
	mzby=[]
	for i, mzion in enumerate(MZbi, start =1):	
		if abs(mz-mzion) <= float(threshold):
			listmzb.append(mz)
			inter = np.array([intense])
			if i not in listb and mzion not in mzby:
				listb.append(i)
				plt.text(mzion, intense, str('b'+str(i)), color = 'red', ha = 'center', zorder =10)
				(markers, stemlines, baseline) = plt.stem(listmzb, inter, linefmt='red', use_line_collection=False, markerfmt=' ', basefmt = '', bottom = 0)
			
	for i, mzion in enumerate(MZyi, start = 1):
		if abs(mz-mzion) <= float(threshold):
			listmzy.append(mz)	
			intery= np.array([intense])
			for mzion in listmzy:
				if mzion in listmzb and i not in listy:
					mzby.append(mzion)
					intyb= np.array([intense])
					listy.append(i)
					plt.text(mzion, intense, str('y'+str(i)+' and'), color = 'blue', position = (mzion, intense+280), ha = 'center', zorder=10)
					(markers, stemlines, baseline) = plt.stem(mzby, intyb, linefmt='orchid', use_line_collection=False, markerfmt=' ', basefmt= '', bottom= 0)
				if mzion not in listmzb and i not in listy:
					mzb = np.array([mzion])
					intb = np.array([intense])
					plt.text(mzion, intense, str('y'+str(i)), color = 'blue', position = (mzion, intense), ha = 'center', zorder=10)
					(markers, stemlines, baseline) = plt.stem(mzb, intb, linefmt='blue', use_line_collection=False, markerfmt=' ', basefmt= '', bottom= 0)
			
					
ax.set_ylim(0, maxi*1.2)
ax.set_xlabel('m/z')
ax.set_ylabel('Relative Abundance')
plt.setp(baseline, 'linewidth', 0, visible= False)
ax.margins(y=0)
plt.title(f'MS/MS Viewer for {peptide}')
plt.show()







