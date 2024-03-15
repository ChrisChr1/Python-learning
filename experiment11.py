import csv
import sys

input1 = sys.argv[1]

f = open('data.csv')
c = csv.DictReader(f, dialect = 'excel')

print('Gene', input1, 'from file data.csv')

count = 0
sum1 = 0
data = {}
data1 = {}

for column in c:
	floatc = float(column[input1])
	sum1 += floatc
	count += 1
	data[count] = sum1
	data1[count] = floatc


for k,v in data.items():
	if k == 112:
		mean = v/k
		print('The mean for this gene is:', mean)
		
var =0
stddev = {}
for k,v in data1.items():
	var += (v-mean)**2
	stddev[k] = var
	if k == 112:
		stddev = (var/111)**0.5
		print('The standard deviation for this gene is:', stddev)
		
	
	
	
	


	

