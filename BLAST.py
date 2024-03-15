# Special modules for running blast
from Bio.Blast.Applications import NcbiblastpCommandline

# Set the blast program and arguments as strings
blast_prog   = '/usr/local/bin/blastp'
blast_query = 'query.fasta'
blast_db    = 'blastdb2/yeast-ribosome.fasta'

# Build the command-line
cmdline = NcbiblastpCommandline(cmd=blast_prog,
                                query=blast_query,
                                db=blast_db,
                                outfmt=5,
                                out="results.xml")
# ...and execute.
stdout, stderr = cmdline()


from Bio.Blast import NCBIXML

result_handle = open("results.xml")


for blast_record in NCBIXML.parse(result_handle):
    score = 1800
    e_value = 1e5
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
                if hsp.expect < e_value:
                    e_value = hsp.expect
                    print('***** Alignment *****')
                    print(f'sequence: {alignment.title}')
                    print('length:', alignment.length)
                    print('e value:', e_value)
                    print(hsp.query[0:75] + '...')
                    print(hsp.match[0:75] + '...')
                    print(hsp.sbjct[0:75] + '...')
                    if hsp.score > score:
                        score = hsp.score
                        print('***** Most Conserved Alignment *****')
                        print(f'sequence: {alignment.title}')
                        print('score:', score)
                        print('e value:', hsp.expect)
                        print(hsp.query[0:75] + '...')
                        print(hsp.match[0:75] + '...')
                        print(hsp.sbjct[0:75] + '...')


