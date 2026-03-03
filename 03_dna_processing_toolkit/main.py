def validate_sequence(dna):
    valid_bases = {'A', 'T', 'G', 'C'}
    return all(base in valid_bases for base in dna)


def reverse_complement(dna):
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    reversed_dna = dna[::-1]
    return ''.join(complement[base] for base in reversed_dna)


def transcribe(dna):
    return dna.replace('T', 'U')


def main():
    dna = input("Enter DNA sequence: ").upper()

    if not validate_sequence(dna):
        print("Invalid DNA sequence! Only A, T, G, C allowed.")
        return

    rev_comp = reverse_complement(dna)
    rna = transcribe(rev_comp)

    print("\n--- Results ---")
    print("Original DNA:        ", dna)
    print("Reverse Complement:  ", rev_comp)
    print("Transcribed RNA:     ", rna)


if __name__ == "__main__":
    main()