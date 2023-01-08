from os import system
from typing import List, Tuple

class node :
    def __init__(self) -> None:
        self.sym = ''
        self.pro = 0.0
        self.arr = [0] * 10
        self.top = 0
        self.result = ''

def shannon(l, h, p):
    pack1 = 0
    pack2 = 0
    diff1 = 0
    diff2 = 0

    if ((l + 1) == h or l == h or l > h):
        if (l == h or l > h): return
        p[h].top += 1
        p[h].arr[(p[h].top)] = 0
        p[l].top+=1
        p[l].arr[(p[l].top)] = 1
    else:
        for i in range(l, h):
            pack1 = pack1 + p[i].pro
        pack2 = pack2 + p[h].pro
        diff1 = pack1 - pack2
        if (diff1 < 0):
            diff1 = diff1 * -1
        j = 2
        while (j != h - l + 1):
            k = h - j
            pack1 = pack2 = 0
            for i in range(l, k + 1):
                pack1 = pack1 + p[i].pro
            for i in range(h,k,-1):
                pack2 = pack2 + p[i].pro
            diff2 = pack1 - pack2
            if (diff2 < 0):
                diff2 = diff2 * -1
            if (diff2 >= diff1): break
            diff1 = diff2
            j += 1
        
        k += 1
        for i in range(l, k + 1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 1
            
        for i in range(k + 1, h + 1):
            p[i].top += 1
            p[i].arr[(p[i].top)] = 0
        
        shannon(l, k, p)
        shannon(k + 1, h, p)
    		
def display(n, p):
    print("\n\n\n\tSymbol\tProbability\tCode",end='')
    for i in range(n - 1, -1, -1):
        print("\n\t", p[i].sym, "\t\t", p[i].pro,"\t",end='')
        for j in range(p[i].top + 1):
            print(p[i].arr[j], end='')
	
if __name__ == '__main__':
    system("cls")
    print("-----------start------------")

    data = ["A", "B", "C", "D", "E", "F"]
    freq = [0.28, 0.22, 0.16, 0.15, 0.14, 0.05]
    result = []

    n = len(data)
    p = [node() for i in range(n)]
    for i in range(n):
        p[i].sym += data[i]
        p[i].pro += freq[i]
        p[i].top = -1

    shannon(0, n - 1, p)
    for i in range(len(p)):
        result.append('')
        for j in range(p[i].top + 1):
            result[i] += str(p[i].arr[j])

    for i in range(len(p)):
        # print(p[i].result)
        print(result[i])

    display(n, p)
