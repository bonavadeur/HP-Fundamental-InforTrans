from os import system
from typing import List, Tuple

# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


def huffman(chars: List, freq: List):
    nodes = []
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    return nodes



def export(node, val='', sym=[], encoded=[]):
    newVal = val + str(node.huff)
    if(node.left):
        export(node.left, newVal, sym, encoded)
    if(node.right):
        export(node.right, newVal, sym, encoded)
    if(not node.left and not node.right):
        sym.append(node.symbol)
        encoded.append(newVal)
        # print(f"{node.symbol} -> {newVal}")
        # print(result)

if __name__ == "__main__":
    system("cls")

    chars = ["A", "B", "C", "D", "E", "F"]
    freq = [0.28, 0.22, 0.16, 0.15, 0.14, 0.05]

    nodes = huffman(chars, freq)

    sym = []
    encoded = []
    export(nodes[0], '', sym, encoded)
    print(sym)
    print(encoded)
    result = [''] * len(chars)
    for i in range(len(chars)):
        idx = chars.index(sym[i])
        result[idx] = encoded[i]
    print(result)
