# -*- coding:utf-8 -*-

import sys
import solver
import asciivision

N=8

def parse_input(str):
    table=[[0 for i in range(8)] for j in range(8)]
    for i in range(0,8):
        for j in range(0,8):
            tmp=str[(i)*9+j]
            if tmp=='N':
                table[i][j]=0
            if tmp=='B':
                table[i][j]=1
            if tmp=='W':
                table[i][j]=2
    return table

fp=open("inputtest.txt",'r')
pretable=fp.read()
got_table=parse_input(pretable)
print asciivision.output(got_table)
greedychoice=solver.greedy_eval(got_table)
print greedychoice
print asciivision.output(solver.transition(got_table,3,0,1))

