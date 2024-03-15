#STEP 2: upload name table
import sys
from model import *

init()

# Read in the names, populate name, class, and id of 
# taxonomy row
h = open(sys.argv[1])
for l in h:
    l = l.strip('\t|\n')        
    sl = l.split('\t|\t')
    taxid = int(sl[0])
    name_class = sl[3]
    name = sl[1]
    t = Taxonomy.byTaxid(taxid)
    n = Name(name=name, name_class=name_class, taxonomy=t)
h.close()
