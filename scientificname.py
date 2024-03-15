import sys
from model import *
init()
try:
    taxid = int(sys.argv[1])
except IndexError:
    print("Need a taxonomy id argument", file=sys.stderr)
    sys.exit(1)
except ValueError:
    print("Taxonomy id should be an integer", file=sys.stderr)
    sys.exit(1)
    
#Get taxonomy row
try:
    t = Taxonomy.byTaxid(taxid)
except SQLObjectNotFound:
    print("Taxonomy id",taxid,"does not exist", file=sys.stderr)
    sys.exit(1)
print("Organism",t.scientific_name,"has rank",t.rank)
for n in t.names:
    print("Organism",t.scientific_name,"has name",n.name)
for c in t.children:
    print("Organism",t.scientific_name,"has child",c.scientific_name,c.taxid)
print("Organism",t.scientific_name,"has parent",t.parent.scientific_name,t.parent.taxid)

r = t
g = None
while r != r.parent:
    if r.rank == 'genus':
        g = r
        break
    r = r.parent

if g == None:
    print("Organism",t.scientific_name,"has no genus")
else:
    print("Organism",t.scientific_name,"has genus",g.scientific_name)
