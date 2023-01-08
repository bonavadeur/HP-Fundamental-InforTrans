from os import system
import math


def binary(a, n):
    result = ''
    for _ in range(n):
        if (a * 2 >= 1):
            result += '1'
            a = a * 2 - 1
        else:
            result += '0'
            a = a * 2
    return result


if __name__ == "__main__":
    system("cls")
    data = ["A", "B", "C", "D", "E", "F"]
    freq = [0.28, 0.22, 0.16, 0.15, 0.14, 0.05]
    n = len(freq)
    Pi = 0
    b = []
    result = []
    for i in range(n):
        b.append(math.ceil(0 - math.log(freq[i], 2)))
        result.append(binary(Pi, b[i]))
        Pi += freq[i]
    print(result)