# -*- coding:utf-8 -*-

import solver
from solver import transition
from solver import judge_constant
from copy import deepcopy

def const_f(p,q,table,color):
    """
    The number of constant stone
    counting new constant stones with table[p][q]
    """
    ope_table=deepcopy(table)
    cr_count=0
    for i in range(N):
        for j in range(N):
            if judge_constant(ope_table,i,j,color)==1:
                cr_count+=1
            else:
                #do nothing
                pass

    nx_table=transition(ope_table,p,q,color)
    nx_count=0
    for i in range(N):
        for j in range(N):
            if judge_constant(nx_table,i,j,color)==1:
                nx_count+=1
            else:
                pass
    return nx_count-cr_count
    
    

def potential_f(p,q,table):
    """
    The number of potential getting stone
    """


    
