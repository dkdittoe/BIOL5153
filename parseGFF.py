#! /usr/bin/env python

#add parse argument

import argparse

#create and argumentparser object ('parser') that will hold all of the information necessary to parse the command line
parser = argparse.ArgumentParser(description='generates genetic code from genome for each feature')

#add optional arguments
# -- infront of argument identifies it as optional
parser.add_argument('-d', '--my_data', help='the .gff  file', default= 'watermelon.gff')
parser.add_argument('-d2', '--data2', help='the .fsa file', default = 'watermelon.fsa')

#parse the command line arguments
args = parser.parse_args()

my_data = open(args.my_data, "r")
data2 = open(args.data2, "r")

#read gff line by line
for line in my_data:
    #skip blank lines

    #remove line breaks
    line = line.rstrip("\n")
    
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
