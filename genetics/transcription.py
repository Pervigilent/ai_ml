amino_acids = [
    ("Alanine", "Ala", 'A'),
    ("Arginine", "Arg", 'R'),
    ("Asparagine", "Asn", 'N'),
    ("Aspartate", "Asp", 'D'),
    ("Cysteine", "Cys", 'C'),
    ("Glutamine", "Gln", 'Q'),
    ("Glutamate", "Glu", 'E'),
    ("Glycine", "Gly", 'G'),
    ("Histidine", "His", 'H'),
    ("Isoleucine", "Ile", 'I'),
    ("Leucine", "Leu", 'L'),
    ("Lysine", "Lys", 'K'),
    ("Methionine", "Met", 'M'),
    ("Phenylalanine", "Phe", 'F'),
    ("Proline", "Pro", 'P'),
    ("Serine", "Ser", 'S'),
    ("Threonine", "Thr", 'T'),
    ("Tryptophan", "Trp", 'W'),
    ("Tyrosine", "Tyr", 'Y'),
    ("Valine", "Val", 'V')
]

inverse_codon = {
    ("Ala", 'A') : (("GCU", "GCC", "GCA", "GCG")),
    ("Arg", 'R') : (("CGU", "CGC", "CGA", "CGG"), ("AGA", "AGG")),
    ("Asn", 'N') : (("AAU", "AAC")),
    ("Asp", 'D') : (("GAU", "GAC")),
    ("Asn", "Asp", 'B') : (("AAU", "AAC"), ("GAU", "GAC")),
    ("Cys", 'C') : (("UGU", "UGC")),
    ("Gln", 'Q') : (("CAA", "CAG")),
    ("Glu", 'E') : (("GAA", "GAG")),
    ("Gln", "Glu", 'Z') : (("CAA", "CAG"), ("GAA", "GAG")),
    ("Gly", 'G') : (("GGU", "GGC", "GGA", "GGG")),
    ("His", 'H') : (("CAU", "CAC")),
    ("Ile", 'I') : (("AUU", "AUC", "AUA"))
    ("Leu", 'L') : (("CUU", "CUC", "CUA", "CUG"), "UUA", "UUG")),
    ("Lys", 'K') : (("AAA", "AAG")),
    ("Met", 'M') : (("AUG")),
    ("Phe", 'F') : (("UUU", "UUC")),
    ("Pro", 'P') : (("CCU", "CCC", "CCA", "CCG")),
    ("Ser", 'S') : (("UCU", "UCC", "UCA", "UCG"), ("AGU", "AGC")),
    ("Thr", 'T') : (("ACU", "ACC", "ACA", "ACG")),
    ("Trp", 'W') : (("UGG")),
    ("Tyr", 'Y') : (("UAU", "UAC")),
    ("Val", 'V') : (("GUU", "GUC", "GUA", "GUG")),
    ("START") : (("AUG", "CUG", "UUG")),
    ("STOP") : (("UAA", "UGA", "UAG"))
}

codon = {
    "UUU" : ("Phe", 'F'),
    "UUC" : ("Phe", 'F'),
    "UUA" : ("Leu", 'L'),
    "UUG" : ("Leu", 'L'), # Start codon
    "CUU" : ("Leu", 'L'),
    "CUC" : ("Leu", 'L'),
    "CUA" : ("Leu", 'L'),
    "CUG" : ("Leu", 'L'),
    "AUU" : ("Ile", 'I'),
    "AUC" : ("Ile", 'I'),
    "AUA" : ("Ile", 'I'),
    "AUG" : ("Met", 'M'), # Start codon
    "GUU" : ("Val", 'V'),
    "GUC" : ("Val", 'V'),
    "GUA" : ("Val", 'V'),
    "GUG" : ("Val", 'V'), # Start codon
    "UCU" : ("Ser", 'S'),
    "UCC" : ("Ser", 'S'),
    "UCA" : ("Ser", 'S'),
    "UCG" : ("Ser", 'S'),
    "CCU" : ("Pro", 'P'),
    "CCC" : ("Pro", 'P'),
    "CCA" : ("Pro", 'P'),
    "CCG" : ("Pro", 'P'),
    "ACU" : ("Thr", 'T'),
    "ACC" : ("Thr", 'T'),
    "ACA" : ("Thr", 'T'),
    "ACG" : ("Thr", 'T'),
    "GCU" : ("Ala", 'A'),
    "GCC" : ("Ala", 'A'),
    "GCA" : ("Ala", 'A'),
    "GCG" : ("Ala", 'A'),
    "UAU" : ("Tyr", 'Y'),
    "UAC" : ("Tyr", 'Y'),
    "UAA" : ("STOP"),
    "UAG" : ("STOP"),
    "CAU" : ("His", 'H'),
    "CAC" : ("His", 'H'),
    "CAA" : ("Gln", 'Q'),
    "CAG" : ("Gln", 'Q'),
    "AAU" : ("Asn", 'N'),
    "AAC" : ("Asn", 'N'),
    "AAA" : ("Lys", 'K'),
    "AAG" : ("Lys", 'K'),
    "GAU" : ("Asp", 'D'),
    "GAC" : ("Asp", 'D'),
    "GAA" : ("Glu", 'E'),
    "GAG" : ("Glu", 'E'),
    "UGU" : ("Cys", 'C'),
    "UGC" : ("Cys", 'C'),
    "UGA" : ("STOP"),
    "UGG" : ("Trp", 'W'),
    "CGU" : ("Arg", 'R'),
    "CGC" : ("Arg", 'R'),
    "CGA" : ("Arg", 'R'),
    "CGG" : ("Arg", 'R'),
    "AGU" : ("Ser", 'S'),
    "AGC" : ("Ser", 'S'),
    "AGA" : ("Arg", 'R'),
    "AGG" : ("Arg", 'R'),
    "GGU" : ("Gly", 'G'),
    "GGC" : ("Gly", 'G'),
    "GGG" : ("Gly", 'G'),
    "GGG" : ("Gly", 'G')
}

start_codon = {
    "UUG" : ("START"),
    "AUG" : ("START"),
    "GUG" : ("START"),
    "UAA" : ("STOP"),
    "UAG" : ("STOP"),
    "UGA" : ("STOP")
}

def antisense(sequence, is_dna=True, reverse=False):
    """
    Generate the antisense (complement) strand for DNA or RNA.

    Parameters:
        sequence (list of str): List of bases (e.g., ['A','T','G','C'] or ['A','U','G','C'])
        is_dna (bool): If True, treat as DNA; otherwise RNA
        reverse (bool): If True, return reverse complement (common biological antisense)

    Returns:
        list of str: Complement (or reverse complement if reverse=True)
    """
    if is_dna:
        complement_map = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
    else:
        complement_map = {
            'A': 'U',
            'U': 'A',
            'C': 'G',
            'G': 'C'
        }

    # Generate complement
    try:
        comp = [complement_map[base.upper()] for base in sequence]
    except KeyError as e:
        raise ValueError(f"Invalid base in sequence: {e}")

    # Optionally reverse for true antisense strand
    if reverse:
        comp = comp[::-1]

    return comp
    
def transcribe(sequence, is_complement=True, reverse=False):
    """
    Transcribe a DNA sequence into RNA.

    Parameters:
        sequence (list of str): DNA bases ['A','T','C','G']
        is_complement (bool): 
            - True  -> produce complementary RNA (biological transcription)
            - False -> just replace T with U (coding strand style)
        reverse (bool):
            - If True, return reversed output (useful for true antisense orientation)

    Returns:
        list of str: RNA sequence
    """
    # Complement mapping for transcription (DNA -> RNA)
    complement_map = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    if is_complement:
        try:
            rna = [complement_map[base.upper()] for base in sequence]
        except KeyError as e:
            raise ValueError(f"Invalid DNA base: {e}")
    else:
        # Coding strand: just replace T with U
        try:
            rna = ['U' if base.upper() == 'T' else base.upper() for base in sequence]
        except Exception as e:
            raise ValueError(f"Invalid DNA sequence: {e}")

    if reverse:
        rna = rna[::-1]

    return rna
    
def reverse_transcribe(sequence, is_complement=True, reverse=False):
    """
    Reverse transcribe an RNA sequence into DNA.

    Parameters:
        sequence (list of str): RNA bases ['A','U','C','G']
        is_complement (bool):
            - True  -> produce complementary DNA (biological reverse transcription)
            - False -> just replace U with T (coding-like strand)
        reverse (bool):
            - If True, return reversed output (useful for orientation control)

    Returns:
        list of str: DNA sequence
    """
    # Complement mapping (RNA -> DNA)
    complement_map = {
        'A': 'T',
        'U': 'A',
        'C': 'G',
        'G': 'C'
    }

    if is_complement:
        try:
            dna = [complement_map[base.upper()] for base in sequence]
        except KeyError as e:
            raise ValueError(f"Invalid RNA base: {e}")
    else:
        # Coding-like strand: just replace U with T
        try:
            dna = ['T' if base.upper() == 'U' else base.upper() for base in sequence]
        except Exception:
            raise ValueError("Invalid RNA sequence")

    if reverse:
        dna = dna[::-1]

    return dna

