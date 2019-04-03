#! /usr/bin/env python

#watermelon.fsa
#watermelon.gff

my_data = open("watermelon.gff", "r")
data2 = open("watermelon.fsa", "r")

#the variable 'genome' holds the genome sequence
genome = " "

#read gff line by line
for line in my_data:
    #skip blank lines

    #remove line breaks
    line = line.rstrip("\n")
    #print(num)
    #split each line on the tab character
    # sequence, source, feature, begin, end, length, strand, phase, attributes = line.split("\t")
    fields = line.split("\t")
    print(fields[3], fields[4])
    start = int(fields[3])
    stop = int(fields[4])
    #extract the dna sequence from the genome for this feature
    substring = data2[start:stop]
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
