import random
from build_blocks import *
from dna_funcs import *

random_DNA = ''.join([random.choice(DNA_Nucleotides)
                       for nuc in range(100)])

test_amino_seq = ['G', 'M', 'N', 'P', 'K', 'L', 'Y', 'V', 'R', 'V', '_', 'I', 'A', 'K', 'S', 'S', 'A', 'V', 'R', 'A', 'L', 'S', 'R', 'R', 'S', 'L', 'M', 'R', 'L', 'D', 'V', 'S']
DNA_seq = validate_seq(random_DNA)

print(f"\nSequence: {len(DNA_seq)}\n")
print(f"[1] + Sequence Length: {len(DNA_seq)}\n ")
print(f"[2] + Nucleotide Frequency: {CountFreq(DNA_seq)}\n")
print(f"[3] + DNA/RNA Transcription: {transcription(DNA_seq)}")
print(f"[4] + DNA string + Reverse complement:\n5' {DNA_seq} 3'")
print(f"   {''.join(['|' for c in range(len(DNA_seq))])}")
print(f"3' {get_complementary_strand(DNA_seq)[::-1]} 5'\n")
print(f"[5] + GC content count: {gc_count(DNA_seq)}\n")
print(f"[6] + GC content percentage: {round(gc_count(DNA_seq)/ len(DNA_seq) *  100)}%\n") 
print(f"[6] + GC content in subsections of the DNA k=5:{gc_content_subsection(DNA_seq,k=5)}\n")
print(f"[7] + Amino Acid seq of the DNA:{translate_seq(DNA_seq)}\n")
print(f"[8] + Codon frequency of L:{codon_usage(DNA_seq,'L')}\n")
print(f"[9] + open reading frames")
for frame in gen_ORF(random_DNA):
    print(frame)

print(f"test for protein gen: {protein_orf(test_amino_seq)}")