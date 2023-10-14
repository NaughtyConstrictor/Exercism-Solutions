CODON_2_PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "",
    "UAG": "",
    "UGA": "",
}
def proteins(strand: str) -> list[str]:
    proteins = []
    iter_codons = [iter(strand)] * 3
    for codon in zip(*iter_codons):
        protein = CODON_2_PROTEIN.get("".join(codon))
        if not protein:
            break
        proteins.append(protein)
    return proteins