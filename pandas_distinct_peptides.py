
import pandas as pd

df= pd.read_csv('proteomics.summary.tsv', sep='\t')

distinct = df.min() >= 2
print('The number of genes with at least two distinct peptides in all samples:',sum(distinct),end='\n\n')
            

distinct2 = df.max() >= 2
print('The number of genes with at least two distinct peptides in at least one sample:', sum(distinct2))


