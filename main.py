# -*- coding:utf-8 -*-

import sys
import solver
import asciivision
import table
from copy import deepcopy
from evaluatefuncs import const_f
from treemain import maxroute

N=8
PLAYER=1
COMPUTER=2

STEP=4

def parse_input(str):
    table=[[0 for i in range(N)] for j in range(N)]
    for i in range(0,N):
        for j in range(0,N):
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
    greedychoice=solver.greedy_eval(got_table,1)
##    print "----greedy choice------>>"
  ##  print greedychoice
    print "----Calcutating.......please wait a minute-->>"
    answer_c=maxroute(const_f,got_table,1,STEP)
    print "------constant choice---->>"
    print answer_c
    got_table=solver.transition(deepcopy(got_table),answer_c[0],answer_c[1],1)
    print "----Calc....RESULT---->>>"
    print asciivision.output(got_table)
    print "----constant matrix-------"
    c=deepcopy(got_table)
    print asciivision.output(solver.constant_matrix(c,2))
    print "----You can set these point below-----"
    print asciivision.output_num(solver.possible_area(got_table,2))
    print "----current table---------"
    print asciivision.output(got_table)
    print "Your color:○"
    """
    consttable=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            consttable[i][j]=const_f(i,j,got_table,2)
    """
