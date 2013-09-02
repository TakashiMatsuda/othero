# -*- coding:utf-8 -*-

import sys
import solver
import asciivision

N=8
PLAYER=1
COMPUTER=2

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

def parse_output(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            f=0

fp=open("inputtest.txt",'r')
pretable=fp.read()
got_table=parse_input(pretable)
print asciivision.output(got_table)


print "Your color:○" 
while(True):
    order1=int(raw_input(">入力待ち:行"))
    order2=int(raw_input(">入力待ち:列"))
    got_table=solver.transition(got_table,order1,order2,2)
    print "----transition by you->>>"
    print asciivision.output(got_table)
    greedychoice=solver.greedy_eval(got_table)
    print greedychoice
    result=solver.transition(got_table,greedychoice[0],greedychoice[1],1)
    print "----Calc....RESULT---->>>"
    print asciivision.output(result)
    print "----constant matrix----"
    print asciivision.output(solver.constant_matrix(result,1))
    

