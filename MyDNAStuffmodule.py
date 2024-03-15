
def readseq(seqfile):
    theseq = ''.join(open(seqfile).read().split())
    theseq = theseq.upper()
    return theseq

def codontable(codonfile):
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
    return codons, init

def get_ambig_aa(codontab, codon):
    try:
        aas = set()
        for n3 in 'ACGT':
            codon1 = codon[:2]+n3
            aas.add(codontab[codon1])
    except:
        if len(aas) > 1:
            return 'x'
    return aas.pop().lower()

def comp(seq):
    c = []
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
    for nuc in seq:
        c.append(comp.get(nuc,nuc))
    cseq = ''.join(c)
    return cseq

def revComp(seq):
    rc = []
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
    for nuc in reversed(seq):
        rc.append(comp.get(nuc,nuc))
    rcseq = ''.join(rc)
    return rcseq

def trans(codons,seq,frame, st):
    seq += 'N'*(frame-1)
    aalist = []
    starts = []
    for i in range(frame-1,len(seq),3):
        codon = seq[i:i+3]
        if codon in codons:
            aa = codons[codon]
            start = st.get(codon, 'X')
            if start == True:
                starts.append(start)
        elif len(codon) < 3:
            aa = ''
        elif codon.count('N') == 1 and codon[2] =='N':
            aa = get_ambig_aa(codons,codon)
        else:
            aa = 'X'
        aalist.append(aa)
    aaseq = ''.join(aalist)
    print('There are', sum(starts), 'potential start codons in')
    return aaseq

def freq(seq):
	counts = {}
	for nuc in seq:
		if nuc not in counts:
			counts[nuc] = 0
		counts[nuc] += 1
	for k,v in sorted(counts.items(), key=lambda p:p[1], reverse = True):
		print('The frequency of nucleotide', k, 'is', v, end= '\n\n')

def atg(seq):
	seq = seq.lower()
	atgpos = seq.find('atg')
	frame = (atgpos%3) + 1
	print('There is a start codon in forward frame', frame)
           

