from sqlobject import *
import os.path, sys

dbfile = 'small_taxa.db3'


conn_str = os.path.abspath(dbfile)
conn_str = 'sqlite:'+ conn_str
sqlhub.processConnection = connectionForURI(conn_str)

class Taxonomy(SQLObject):
    class sqlmeta: 
        fromDatabase = True

class Name(SQLObject):
    class sqlmeta:
        fromDatabase = True
    

name = sys.argv[1]
condition = (Name.q.name == f"{name}")

for n in Name.select(condition):
	taxa_id = n.taxonomyID
	condition = (Taxonomy.q.id == taxa_id)
	taxa = Taxonomy.select(condition)
	for n in taxa:
		print(n.scientificName)


