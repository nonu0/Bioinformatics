from build_blocks import *
from collections import Counter

def validate_seq(seq):
    temp_seq=seq.upper()
    for nuc in temp_seq:
        if nuc not in DNA_Nucleotides:
            return False
    return temp_seq


#counts the frequency of each nucleotide
def CountFreq(seq):
    temp_data = {'A':0,'C':0,'G':0,'T':0}
    for nuc in seq:
        temp_data[nuc] += 1
    return temp_data

# gets the complementary strand
def get_complementary_strand(seq):
    return ''.join([complementary_strand[nuc] for nuc in seq])[::-1]

# transcribes the seuence given 
def transcription(seq):
    return seq.replace('T','U')

def gc_count(seq):
    """
        function to count the GC content in a DNA/RNA sequence
    """
    return round((seq.count('C') + seq.count('G')))

def gc_content_subsection(seq,k=20):
    res = []
    for i in range(0,len(seq)-k+1,k):
        subseq=seq[i:i+k]
        res.append(gc_count(subseq))
    return res

def translate_seq(seq,init_pos=0):
    """translate DNA seq to an amino acid seq"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos,len(seq) - 2,3)]

def codon_usage(seq,aminoacid):
    """gives the frequency of each codon coding for a given amino acid"""
    tempList = []
    for i in range(0,len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tempList.append(seq[i:i + 3])
            print(tempList)

    freqDict = dict(Counter(tempList))
    print(freqDict)
    total = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / total,2)
    return freqDict

def gen_ORF(seq):
    frames = []
    frames.append(translate_seq(seq,0))
    frames.append(translate_seq(seq,1))
    frames.append(translate_seq(seq,2))
    frames.append(translate_seq(get_complementary_strand(seq),2))
    frames.append(translate_seq(get_complementary_strand(seq),1))
    frames.append(translate_seq(get_complementary_strand(seq),2))
    return frames

def protein_orf(aa_seq):
    """compute all possible proteins in an amino acid sequence and return all possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == '_':
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            if aa == 'M':
                current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i] += aa
    return proteins
