dna = "ATGCGTACGTTAG"

g = dna.count("G")
c = dna.count("C")

gc_content = (g + c) / len(dna) * 100

print("DNA Sequence:", dna)
print("GC Content:", gc_content)