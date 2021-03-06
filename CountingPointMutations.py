#Counting Point Mutations(Hamming Distance)
DNAseq1="TTCGGAATCCGCTACCCGGTGGGGCTCATCCCGAGTGTCCTCCGCGTCGTAGGAACTCCTCGGTACAGGTCTGTGTTGACAAACCCAACGGTCCCTACATAAACCAATCATTTAGCGCTCAAATAATTTGCGAAGATTAGTGGCCTGACGAACACTGCATACAGAGCGGCCTAGATGGTTTCGACATACCTGTCGACGGCTTAATTATAGCAGGCCACGTTACACGGTTGCGATATCACACCTTTTCATGAAGTTAAGCAGTGGACCACAAGAGAAGTCCTCATCAGATGAAATACGAGGACGCCGAGTACCACAGTTCAGGGCGGCGACACACAAGCCTACTCTGAGATAGTCGGCATCTACAGAAACTAAGTTGAGTACTAGAGTTTAATGAAAGACATACGCGGGTCCAAAAAATTACCGTAAGCGCGCGAGCATCCCTGCCAGCAGAAATCTTAACACCTCGGACAGTCGAGTACATCCGAACTAGAATGCAATGCTGGCAATCTTGTGATTGTACACCAGCGACGCCGAGCTGTAAATGCGACTTATAATAGACTTGCGATATCTCAATGAACAACCTGAGTGAAAACGAGCCTAGTGCTCGTTGTCGCTTGAACGGGCTAAAGGTGAAGGTCAAAAGAGATAGTGCGCTGTCTCCGGGGTGGGCGACCGCACTTGTCTGGTGCAAATACGATTGGACTCCTCACTAAAGCGTATGCGTTGCAGATGGCCTCTGACCCCTCCAGTGAATCCTAACCTTAACCGTCGGTTGAGGGCCTTCGTGAAGACGTTTTTAAGAGCGTGCGTATAAGGCCTGGCTATTGCCCGGCCAGGCACTTTCCAAGGATGCTTGCAACATCGGATCAGCATCCAGGACGCTTTATGACCAAGATAATCCAAA"
DNAseq2="TCGGGAAGGTTCACACTGATTATGCTCCTCTCTTATTAATTCCTCTCCCAACCAGGCCCTAAGTAGCGCGCCTCGTATTGGAACCCTAAGACACGTAATGCAGTTATTACGGGAGAGCAAAGCTAGTGTCGGTAGAGTGGGGGACCTATGCTAAGGGCGTTCTGATCACATTTGGTGCTTTCCACAGTGCTTCCATCAAATTTTCCGGTTCATCCACCATTACAGGGCTACGAAACGAAGTTTTTTCGGGAGATTGAGATAATCTCAACAATACCAGAAAATATGAGATGACACACAACTACTCCCGTCAACGCCCTTCAGTATTCCGACTCCCGAGCCAAATTTAAAAATTACGGGTTCTAGCGAGACGACACGTTGTGACGGAGTAGGCAGACACACAGTTGCGGATACAACAGGTCTTTCTAAGCGCCTGTACGTCGCATCAGGCACACGGCTGGATGTCTGGGCCCTTCAAATACTTTTGGACTAGTAAACCATACGGAGCATCAAGCGGTTGATCGACTGCGAAGGTGGTGACTTAATGATACTTATTATAGACTTACAATACGTTGATCGATACCATTCGTACTACCGAATGAAGTGTGTATCGATTTCCCTAAATGCCCGAGGTGTTTCGCGAAAGTCATTTCGCGCTTTATCCTTATTGACCGACCGCACGTCTCTTCATTATACCCAGTCGAGGATCTGTCCCACCCTTTTGCTCTGCGCGTGGGCTCTCCACCCCCCATAGGACGCTACCCCTGACGATCTGTTTCAGGCTCAATGCTAGACGTTTACAAAGGCTTGCTCACTTACCCAGTCAATTGACCGTCCAGGAACAACTAATGGTAGTTAGCATTATCTACTCGCCATTCAGTCTGCTGTATCGAACGGGGATATTAAC"
HammingDistance=0
for i in range(len(DNAseq1)):
    if DNAseq1[i]!=DNAseq2[i]:
        HammingDistance+=1
    else:
        pass
print(HammingDistance)

#Alternative 1 liner solution
print(sum([a!=b for a,b in zip(DNAseq1,DNAseq2)]))

