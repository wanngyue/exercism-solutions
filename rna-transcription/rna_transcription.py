# C > G
# G > C
# T > A
# A > U
def to_rna(dna_strand):
    dict = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
    return ''.join([dict.get(c, c) for c in dna_strand])
