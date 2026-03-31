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
    "UUG" : ("Leu", 'L'),
    "CUU" : ("Leu", 'L'),
    #TODO: Finish
    "GGG" : ("Gly", 'G')
}

