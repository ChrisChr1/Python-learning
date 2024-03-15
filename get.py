from model import *
init()

try:
   #hs = Taxonomy.get(7921)
   hs = Taxonomy.byTaxid(9606)
except SQLObjectNotFound:
   # if row id 7921 / Tax id 9606 is not in table...
   print("Bad taxonomy lookup")

print(hs)
results = Taxonomy.selectBy(taxid=9606)
if results.count() == 0:
   # No rows satisfy the constraint!
   print("Bad taxonomy lookup")

try:
   first_item = results[0]
except IndexError:
   # No first item in the results
   print("Bad taxonomy lookup")

print(first_item)
