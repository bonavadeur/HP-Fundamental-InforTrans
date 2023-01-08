# from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import math


class Algorithm(ABC):
    @abstractmethod
    def execute(self, data: List, freq: List) -> List:
        pass

class FanoDataStruct :
    def __init__(self) -> None:
        self.sym = ''
        self.pro = 0.0
        self.arr = [0] * 20
        self.top = 0
        self.result = ''
class Fano(Algorithm):
    def fano(self, l, h, p):
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
            return
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
            
            self.fano(l, k, p)
            self.fano(k + 1, h, p)

    def execute(self, data: List, freq: List) -> List:
        result = []
        n = len(data)
        p = [FanoDataStruct() for _ in range(n)]
        for i in range(n):
            p[i].sym += data[i]
            p[i].pro += freq[i]
            p[i].top = -1
        self.fano(0, n - 1, p)
        for i in range(len(p)):
            result.append('')
            for j in range(p[i].top + 1):
                result[i] += str(p[i].arr[j])
        return result


class HuffmanDataStruct:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
class Huffman(Algorithm):
    def huffman(self, chars: List, freq: List):
        nodes = []
        for x in range(len(chars)):
            nodes.append(HuffmanDataStruct(freq[x], chars[x]))
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes[0]
            right = nodes[1]
            left.huff = 0
            right.huff = 1
            newNode = HuffmanDataStruct(left.freq + right.freq, left.symbol + right.symbol, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
        return nodes

    def export(self, node, val='', sym=[], encoded=[]):
        newVal = val + str(node.huff)
        if(node.left):
            self.export(node.left, newVal, sym, encoded)
        if(node.right):
            self.export(node.right, newVal, sym, encoded)
        if(not node.left and not node.right):
            sym.append(node.symbol)
            encoded.append(newVal)

    def execute(self, data: List, freq: List) -> List:
        id = list(range(len(data)))
        nodes = self.huffman(id, freq)
        # nodes = self.huffman(data, freq)
        sym = []
        encoded = []
        self.export(nodes[0], '', sym, encoded)
        result = [''] * len(id)
        for i in range(len(id)):
            idx = id.index(sym[i])
            result[idx] = encoded[i]
        return result

class Shannon(Algorithm):
    def binary(self, a, n):
        res = ''
        for _ in range(n):
            if(a * 2 >= 1):
                res += '1'
                a = a * 2 - 1
            else:
                res += '0'
                a = a * 2
        return res

    def execute(self, data: List, freq: List) -> List:
        Pi = 0
        b = []
        result = []
        for i in range(len(freq)):
            b.append(math.ceil(0 - math.log(freq[i], 2)))
            result.append(self.binary(Pi, b[i]))
            Pi += freq[i]
        return result