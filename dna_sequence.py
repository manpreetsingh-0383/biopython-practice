dna = "ATGCCGTA"

complement = dna.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()

reverse_complement = complement[::-1]

print("DNA Sequence:", dna)
print("Reverse Complement:", reverse_complement)