# -*- coding:utf-8 -*-


def output(table):
    L=[]
    L.append(" １ ２ ３ ４ ５ ６ ７ ８\n")
    for i in range(8):
        L.append(str(i+1))
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
