# -*- coding: utf-8 -*-
import sys
from model.Model import FA

from service.DFAService import *
from service.NFAService import *

def NFAToDFA():
    # input_k = 0
    # print "please input item for k,end with -1\n"
    # k=set()
    # while (input_k != -1):
    #     input_k = input(int)
    #     k.add(input_k)
    # input()
    # input_sigma = ''
    # print "please input alphabet for sigma,end with '#'\n"
    # sigma =set()
    # while(input_sigma != '#'):
    #     input_sigma = input_sigma
    #     sigma.add(input_sigma)

    k = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    sigma = {'a', 'b'}

    nfa = FA(sigma)

    nfa.setK(k)

    s = {0}

    nfa.setS(s)

    z = {10, }

    nfa.setZ(z)

    f = {}

    for i in range(11):
        f[i] = {}
    f[0]['::e::'] = {1, 7}
    f[1]['::e::'] = {2, 4}
    f[2]['a'] = {3, }
    f[3]['::e::'] = {6, }
    f[4]['b'] = {5, }
    f[5]['::e::'] = {6, }
    f[6]['::e::'] = {1, 7}
    f[7]['a'] = {8, }
    f[8]['b'] = {9, }
    f[9]['b'] = {10, }

    nfa.setF(f)




    dfa = FA()

    dfa = NFA_to_DFA(nfa)

    simple_dfa = simplify(dfa)

    print 1