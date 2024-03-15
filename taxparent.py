import sys
from model import *

init()

# Read in the taxonomy nodes, get self and parent taxonomy objects,
# and fix the parent field appropriately
h = open(sys.argv[1])
for l in h:
    l = l.strip('\t|\n')        
    sl = l.split('\t|\t')
    taxid = int(sl[0])
    parent_taxid = int(sl[1])
    t = Taxonomy.byTaxid(taxid)
    p = Taxonomy.byTaxid(parent_taxid)
    t.parent = p
h.close()

# Find all scientific names and fix their taxonomy objects' scientific
# name files appropriately
for n in Name.select(Name.q.name_class == 'scientific name'):
    n.taxonomy.scientific_name = n.name
