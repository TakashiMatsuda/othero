# -*- coding:utf-8 -*-


def output(table):
    L=[]
    L.append(" ０ １ ２ ３ ４ ５ ６ ７\n")
    for i in range(8):
        L.append(str(i))
        for j in range(8):
            if table[i][j]==0:
                L.append("　 ")
            if table[i][j]==1:
                L.append("● ")
            if table[i][j]==2:
                L.append("○ ")
        L.append('\n')
    s=''.join(L)
    return s
