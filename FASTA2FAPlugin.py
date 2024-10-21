#!/usr/bin/python2

import sys
import os

class FASTA2FAPlugin:
 def input(self, inputfile):
     self.in_filename = inputfile
 def run(self):
     pass
 def output(self, outputfile):
    in_filename = self.in_filename
    out_filename = outputfile
    infile = open(in_filename,'r')
    outfile = open(out_filename,'w')
    indexfile = open(out_filename+".readname",'w')

    i=1
    for line in infile:
     if line[0]=='>':
         if i>1:
             outfile.write('\n')
         outfile.write('>'+str(i)+'\n')
         indexfile.write(str(i)+'\t'+line[1:-1]+'\n')
         i+=1
     else:
         outfile.write(line.strip())
    outfile.write('\n')

    indexfile.close()
    outfile.close()
    infile.close()
    ################################################################################
    
