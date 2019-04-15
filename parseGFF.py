#! /usr/bin/env python3

#------------------------------------------------

#the variable 'genome' holds the genome sequence
genome = []

#------------------------------------------------

# bio python to parse fsa file
from Bio import SeqIO

fasta_sequences = SeqIO.parse(open('watermelon.fsa'),'fasta')
for fasta in fasta_sequences:
    name, sequence = fasta.id, str(fasta.seq)

#------------------------------------------------

#csv to parse gff file
import csv

#open data file
with open('watermelon.gff', 'r') as gff_file:

	#create a csv reader object
	#have to give the reader what the delimiter is, i.e. comma 
	csvreader = csv.reader(gff_file, delimiter='\t')
	
	#split into a list and can now access column, by column...parsed the file
	for line in csvreader:
	#conditional formatting to skip empty lines
		if not line:
			continue
		else:		
			start = int([3])
    		stop = int([4])


#---------------------------------------------------

            #extract the dna sequence from the genome for this feature
            substring = sequence[start:stop]
            genome = genome + substring
            print(genome)

            #print GC content
            G = str(genome).count('G')
            C = str(genome).count('C')
            total = len(str(genome))
            GC_total = G+C
            GC_content = GC_total/total
            print(GC_content)

#write the code for extracting the substring
#caculate the GC content for this feature, and print it to the screen
#save it, track it with GIT, push it to GIThub. We will continue to modify and upload to GITHUB
