
# coding: utf-8

# In[3]:

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
coding = open("coding.txt", "w")
coding.write("intron:")
coding.write(dna_seq[62:90])
coding.close()

non_coding = open("non_coding.txt", "w")
non_coding.write("exon1:")
non_coding.write(dna_seq[0:62])
non_coding.write("\n")
non_coding.write("exon2:")
non_coding.write(dna_seq[90:1000])
non_coding.close()


# In[6]:

FASTA = open("fasta_example.fasta", "w")
FASTA.write(">ABC123")
FASTA.write("\n")
FASTA.write("ATCGTACGATCGATCGATCGCTAGACGTATCG")
FASTA.write("\n")
FASTA.write(">DEF456")
FASTA.write("\n")
FASTA.write("actgatcgacgatcgatcgatcacgact".upper())
FASTA.write("\n")
FASTA.write(">HIJ789")
FASTA.write("\n")
FASTA.write("ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-", ""))
FASTA.write("\n")
FASTA.close()


# In[7]:

ABC123 = open("ABC123.fasta", "w")
ABC123.write(">ABC123")
ABC123.write("\n")
ABC123.write("ATCGTACGATCGATCGATCGCTAGACGTATCG")
ABC123.close()
DEF456 = open("DEF456.fasta", "w")
DEF456.write(">DEF456")
DEF456.write("\n")
DEF456.write("actgatcgacgatcgatcgatcacgact".upper())
DEF456.close()
HIJ789 = open("HIJ789.fasta", "w")
HIJ789.write(">HIJ789")
HIJ789.write("\n")
HIJ789.write("ACTGAC-ACTGT--ACTGTA----CATGTG".replace("-", ""))
HIJ789.close()


# In[ ]:



