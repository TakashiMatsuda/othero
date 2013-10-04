# -*- coding:utf-8 -*-

import solver
from solver import transition
from solver import judge_constant
from copy import deepcopy

N=8

def const_f(p,q,table,color):
    """
    The number of constant stone powered by potential_f
    counting new constant stones with table[p][q]
    """
    ope_table=deepcopy(table)
    cr_count=0
    for i in range(N):
        for j in range(N):
            if judge_constant(ope_table,i,j,color)==1:
                #cr_count+=1
                cr_count+=potential_f(deepcopy(ope_table),i,j,color)
            else:
                #do nothing
                pass

    nx_table=transition(ope_table,p,q,color)
    nx_count=0
    for i in range(N):
        for j in range(N):
            if judge_constant(nx_table,i,j,color)==1:
                nx_count+=potential_f(deepcopy(ope_table),i,j,color)
            else:
                pass
    return nx_count-cr_count
    
    

def potential_f(table,p,q,color):
    """
    The number of constant and dynamic stone potentially get in the future
    2 step number
    """
    """
    risk function will be available, it will improve the stone score.
    """
    



def risk(table,p,q,color):
    """
    The number of stones robbed together with [p,q] for all direction
    """
    
