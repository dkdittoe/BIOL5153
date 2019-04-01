
# coding: utf-8

# In[16]:

filename = open("input.txt")

#print
for dna in filename:
    print(dna)


# In[24]:

filename = open("input.txt")
output = open("trimmed_sequence.txt", "w")

for dna in filename:
    last_character = len(dna)
    sequence = dna[14:last_character]
    output.write(sequence)
    print("Sequence length " + str(len(sequence))) 


# In[26]:

exon = open("exons.txt")

for line in exon:
    print(line)


# In[29]:

exon = open("exons.txt")

for line in exon:
    num = line.split(',')
    print(num)


# In[30]:

exon = open("exons.txt")

for line in exon:
    num = line.split(',')
    start = num[0]
    stop = num[1]
    print("start is " + start + ", stop is " + stop)


# In[38]:

dna = open("genomic_dna.txt").read()
exon = open("exons.txt")
coding_seq = ""



for line in exon:
    num = line.split(',')
    start = int(num[0])
    stop = int(num[1])
    exon_seq = dna[start:stop]
    coding_seq = coding_seq + exon_seq
    
output = open("coding_seq.txt", "w")
output.write(coding_seq)
output.close()


# In[ ]:



