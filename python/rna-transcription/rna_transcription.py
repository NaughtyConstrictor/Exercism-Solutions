DNA_2_RNA = str.maketrans("GCTA", "CGAU")

def to_rna(dna_strand: str) -> str:
    """Converts a dna strand into an rna strand.

    Parameters
    ----------
    dna_strand:
        A dna strand.

    Returns
    -------
    The rna strand corresponding to the input dna.
    """

    return dna_strand.translate(DNA_2_RNA)