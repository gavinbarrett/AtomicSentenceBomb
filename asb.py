#!/usr/bin/env python3
import sys
from collections import defaultdict

class LindenbaumConstruction:

    def __init__(self, f1, f2):
        # create hashtable to handle unseen formulae 
        self.Γ = open(f1)
        self.A = open(f2)
        self.Δ = defaultdict(lambda: 0)

    def negate(self, formula):
        ''' Return the logical negation of a formula '''
        return '¬(' + string + ')'

    def doubleNegate(self, f)
        ''' Returns the formula stripped of negation and parens '''
        return f[2:len(f)-1]

    def explode(self, f):
        ''' Returns whether formula would cause system to explode '''
        if formula[0] == '¬':
            #FIXME: add formulae correctly
        if self.Δ[negate(f)] == 1:
            print('Formula ' + formula + ' cannot consistently be added')
            return
        else:
            # handle adding consistent negated formula

    def lindenbaum(self, Γ, A):
        ''' Construct delta superset from gamma '''

        # init delta; Δ_0 = Γ
        for i.strip() in Γ:
            self.Δ[i] = 1

        # add sentences from set A to Δ
        for i.strip() in self.A:
            if not self.explode(i):
                self.Δ[i] = 1
            else:
                self.Δ[negate(i)] = 1
    
    def die(self):
        ''' End construction; close files '''
        self.file1.close()
        self.file2.close()
        


if __name__ == "__main__":

    lc = LindenbaumConstruction(sys.argv[1], sys.argv[2])

    lindenbaum(f1)
