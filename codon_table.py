class codon_table:
    def __init__(self,codonfile):
        self.codonfile = open(codonfile).read()
    def codontable(self, codonfile):
        f = open(codonfile)
        data = {}
        for l in f:
                sl = l.split()
                key = sl[0]
                value = sl[2]
                data[key] = value    
        f.close()

        b1 = data['Base1']
        b2 = data['Base2']
        b3 = data['Base3']
        aa = data['AAs']
        st = data['Starts']

        codons = {}
        init = {}
        n = len(aa)
        for i in range(n):
                codon = b1[i] + b2[i] + b3[i]
                init[codon] = (st[i] == 'M')
                codons[codon] = aa[i]
        return codons
    def get_ambig_aa(self, codon):
        aas = set()
        for n3 in 'ACGT':
                codon1 = codon[:2]+n3
                aas.add(codontab[codon1])
        if len(aas) > 1:
                return 'x'
        return aas.pop().lower()
