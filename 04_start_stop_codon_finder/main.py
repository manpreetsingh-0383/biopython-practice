dna = input("Enter DNA sequence: ").upper()

start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

print("\nStart Codons Found:")

for i in range(len(dna) - 2):
    codon = dna[i:i+3]

    if codon == start_codon:
        print(f"Position {i+1}: {codon}")

print("\nStop Codons Found:")

for i in range(len(dna) - 2):
    codon = dna[i:i+3]

    if codon in stop_codons:
        print(f"Position {i+1}: {codon}")
