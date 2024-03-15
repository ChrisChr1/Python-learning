from sqlobject import *
import os.path, sys

dbfile = 'small_taxa.db3'

def init(new=False):
    # Magic formatting for database URI
    conn_str = os.path.abspath(dbfile)
    conn_str = 'sqlite:'+ conn_str
    # Connect to database
    sqlhub.processConnection = connectionForURI(conn_str)
    if new:
        # Create new tables (remove old ones if they exist)
        Taxonomy.dropTable(ifExists=True)
        Name.dropTable(ifExists=True)
        Taxonomy.createTable()
        Name.createTable()
#create two tables: Taxonomy and Name inheriting from SQLObject. Taxonomy will have four columns. Name will have three columns.
class Taxonomy(SQLObject):
    taxid = IntCol(alternateID=True)
    scientific_name = StringCol()
    rank = StringCol()
    parent = ForeignKey("Taxonomy")#foreign key that is the identity of the row. Because you’re interested in the entire row.Consider it to be like a pointer. 

class Name(SQLObject):
    taxonomy = ForeignKey("Taxonomy")#points to table
    name = StringCol()
    name_class = StringCol()
