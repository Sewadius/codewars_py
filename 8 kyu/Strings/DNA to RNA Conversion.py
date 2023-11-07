def dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


print(dna_to_rna('GCAT'))       # -> 'GCAU'
print(dna_to_rna('TTTT'))       # -> 'UUUU'
