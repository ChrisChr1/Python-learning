class DNASeq:
    def __init__(self, seq):
        self.seq = ''.join(open(seq).read().split())
    def comp(self, seq):
        c = []
        comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
        for nuc in seq:
            c.append(comp.get(nuc,nuc))
        cseq = ''.join(c)
        return cseq
    def revComp(self, seq):
        rc = []
        comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
        for nuc in reversed(seq):
            rc.append(comp.get(nuc,nuc))
        rcseq = ''.join(rc)
        return rcseq
    def trans(self, seq, codons, frame):
        seq += 'N'*(frame-1)
        aalist = []
        starts = []
        for i in range(frame-1,len(seq),3):
            codon = seq[i:i+3]
            if codon in codons:
                aa = codons[codon]
            elif len(codon) < 3:
                aa = ''
            else:
                aa = 'X'
            aalist.append(aa)
        return ''.join(aalist)
    def freq(self, seq):
        counts = {}
        for nuc in seq:
            if nuc not in counts:
                counts[nuc] = 0
            if nuc in counts:
                counts[nuc] += 1
        return counts
    def atg(self, seq):
        seq = seq.lower()
        atgpos = seq.find('atg')
        frame = (atgpos%3) + 1
        return frame

