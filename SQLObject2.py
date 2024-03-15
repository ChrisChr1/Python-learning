from sqlobject import *
import os.path, sys

dbfile = 'small_taxa.db3'

conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:'+ conn_str
sqlhub.processConnection = connectionForURI(conn_str)
#create two tables: Taxonomy and Name inheriting from SQLObject. Taxonomy will have four columns. Name will have three columns.
class Taxonomy(SQLObject):
    taxid = IntCol(alternateID=True)
    scientific_name = StringCol()
    rank = StringCol()
    parent = ForeignKey("Taxonomy")#foreign key that is the identity of the row. Because you’re interested in the entire row.Consider it to be like a pointer. 
    names = MultipleJoin("Name")
    children = MultipleJoin("Taxonomy",joinColumn='parent_id')
class Name(SQLObject):
    taxonomy = ForeignKey("Taxonomy")#points to table
    name = StringCol()
    name_class = StringCol()

try:
	name = sys.argv[1]
	condition = (Name.q.name == f"{name}")
except IndexError:
	print("Need to input a common name", file=sys.stderr)
	sys.exit(1)
	
species = []
for n in Name.select(condition):
	taxid = n.taxonomyID
	taxa = Taxonomy.select(Taxonomy.q.id == taxid)
	for t in taxa:
		x = t.scientific_name
		species.append(x)
try:
	r = t
	print('\n==== Taxonomic Lineage for', name ,'====')
except NameError:
	print(name, 'does not exist in database. Check spelling and try again', file=sys.stderr)
	sys.exit(1)

g = None
lineage = []
while r != r.parent:
	if r.rank == 'superkingdom':
		g = r
		break
	r = r.parent
	lineage.append(r.scientific_name)
lineage = lineage[::-1]
print(', '.join(lineage), sep =',')
print('\nExtant Species:', ', '.join(species))


