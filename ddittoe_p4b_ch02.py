
# coding: utf-8

# In[4]:

#DNA sequence given in exercises
dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#print out AT content
A = dna_seq.count("A")
T = dna_seq.count("T")
total = len(dna_seq)
AT_total = A+T
AT_content = AT_total/total
print(AT_content)



# In[5]:

#complement the given DNA strand
dna_seq2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

print(dna_seq2.replace("A" "C" "T" "G", "T" "G" "A" "C"))


# In[12]:

# The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
# Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI. 
dna_seq3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#First length
print("Length to G:", dna_seq3[0:21])
#Second length
print("Length from G:", dna_seq3[22:75])



# In[14]:

Length_to_G = "ACTGATCGATTACGTATAGTA"
Length_G_end = "AATTCTATCATACATATATATCGATGCGTTCAT"
print(len(Length_to_G))
print(len(Length_G_end))


# In[15]:

dna_seq4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print("intron:", dna_seq4[62:90])


# In[20]:

dna_seq4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
total = len(dna_seq4)
intron = "ATCGATCGATCGATCGATCGATCATGCT"
intron_length = len(intron)
intron_content = intron_length/total
coding = 1 - intron_content
percent_coding = coding * 100
print(percent_coding)


# In[21]:

dna_seq4 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
intron = dna_seq4[62:90]
exon1 = dna_seq4[0:62]
exon2 = dna_seq4[90:1000]
sequence = exon1 + intron.lower() + exon2
print(sequence)


# In[ ]:



