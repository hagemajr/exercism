def to_rna(dna):
    dna_to_rna = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    try:
        rna_result = [dna_to_rna[x] for x in dna]
    except:
        raise ValueError("Meaningful message indicating the source of the error")
    return "".join(rna_result)