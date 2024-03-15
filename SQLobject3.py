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
    
try: 
	name = sys.argv[1]
	condition = (Name.q.name == f"{name}")
except IndexError:
	print('Type in a valid common name.')
	sys.exit()
except NameError:
	print(name, 'does not exist in this database.')
	sys.exit()


for n in Name.select(condition):
	taxid = n.taxonomyID
	condition = (Taxonomy.q.id == taxid)
	taxa = Taxonomy.select(condition)
	for n in taxa:
		print(n.scientificName)
