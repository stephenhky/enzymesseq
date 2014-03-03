# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:23:30 2014

@author: hok1
"""

from operator import and_
import random as rnd
import argparse

amino_acids_base = 'ARNDCEQGHILKMFPSTWYV'
pos_allowedbases = ['ARNCGHILKFP', 'R', 'RTQILFYV', 'K', 'QNRGHM', 'ATIVL',
                    amino_acids_base, amino_acids_base, amino_acids_base,
                    amino_acids_base, amino_acids_base, amino_acids_base,
                    amino_acids_base]
                   
def enzyme_detected(seq):
    if len(seq) != len(pos_allowedbases):
        raise Exception('length of sequence not equal to '+str(len(pos_allowedbases)))
    return reduce(and_, map(lambda (bases, seqchar): seqchar in bases,
                            zip(pos_allowedbases, seq)))
   
def generate_rnd_seq():
    return ''.join(map(lambda bases: rnd.sample(bases, 1)[0], pos_allowedbases))
   
def get_argparser():
    prog_descp = "Testing Shirley Lee's rule of enzymes"
    parser = argparse.ArgumentParser(description=prog_descp)
    parser.add_argument('--detect', type=str, default=None,
                        help='Determine if the input enzyme can be detected')
    parser.add_argument('--generate', action='store_true',
                        help='Generate random sequences')
    return parser
   
if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()
    
    if args.detect != None:
        print 'Enzyme detected: ', enzyme_detected(args.detect)
    if args.generate:
        for i in range(5):
            print generate_rnd_seq()
