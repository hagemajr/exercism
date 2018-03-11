def distance(original_dna, new_dna):
    if len(original_dna) != len(new_dna):
        raise ValueError("The strings are not the same length.")
    return sum([0 if x == new_dna[i] else 1 for i,x in enumerate(original_dna)])

print(distance("TAG", "GAT"))
