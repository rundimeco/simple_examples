from Bio.Seq import Seq
from Bio import pairwise2

phraseA = "Sur le climat, il n’y a pas de plan B car il n’y a pas de planète B".split()
phraseB = "Climat: Mars n'est pas un plan B pour l'humanité".split()

alignments = pairwise2.align.globalms(phraseA,phraseB,2,-1,-0.5,-0.1, gap_char=["-"])
res = [[align[0],align[1]] for align in alignments]

for r in res:
 print(r[0])
 print(r[1])
 print()


