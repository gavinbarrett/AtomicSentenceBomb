#!/usr/bin/env python3
import sys
from collections import defaultdict

def negate(string):
    ''' Return the logical negation of a formula '''
    return '¬(' + string + ')'

def explode():
    ''' Returns whether formula would cause system to explode '''

def lindenbaum(Γ, A):
    ''' Construct delta superset from gamma '''

    # create hashtable to handle unseen formulae 
    Δ = defaultdict(lambda: 0)

    # init delta; Δ_0 = Γ
    for i.strip() in Γ:
        Δ[i] = 1

    # add sentences from set A to Δ
    for i.strip() in A:
        if not explode():
            Δ[i] = 1
        else:
            Δ[negate(i)] = 1
    f1.close()


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    f1 = open(file1)
    f2 = open(file2)
    lindenbaum(f1)
