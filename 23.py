import sys
import sqlite3

name = sys.argv[1]

conn = sqlite3.connect('taxa.db3')
params = [name]
    
c = conn.cursor()

findid = c.execute("""
   select tax_id from name
   where name = ?;
""", params)

for row in findid:
   taxid = row
   c.execute("""select scientific_name from taxonomy where tax_id = ?""", taxid)
   for row in c:
      print(row[0])


