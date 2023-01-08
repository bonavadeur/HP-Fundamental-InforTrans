# from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from os import system
from random import randrange
import math

from Algorithm import *
from Worker import *



if __name__ == "__main__":
    system("cls")
    print("--------start--------")

    # min_number = int(input("Min: "))
    # max_number = int(input("Max: "))
    # quantity_per_case = int(input("Number tests per case: "))
    min_number = 900
    max_number = 1000
    quantity_per_case = 50

    worker = Worker()

    for case in range(min_number, max_number + 1):
        # system("cls")
        print("processing case = ", case)
        data = ["A"] * case
        avgLength = [0, 0, 0]
        avgPerformance = [0, 0, 0]
        for _ in range(quantity_per_case):
            # your distribution here

            # freq = []
            # sum = 0
            # for j in range(case):
            #     if(j == case - 1):
            #         rand = 10000 - sum
            #     else:
            #         rand = randrange(1, round((10000)/case))
            #     sum += rand
            #     freq.append(rand / 10000)

            freq = [1/case] * case

            # your distribution here

            result_raw = []
            worker.algorithm = Fano()
            li, etp, pfm = worker.evaluation(worker.analyse(data.copy(), freq.copy()), freq.copy())
            result_raw.append(li)
            result_raw.append(pfm)
            avgLength[0] += li
            avgPerformance[0] += pfm

            worker.algorithm = Huffman()
            li, etp, pfm = worker.evaluation(worker.analyse(data.copy(), freq.copy()), freq.copy())
            result_raw.append(li)
            result_raw.append(pfm)
            avgLength[1] += li
            avgPerformance[1] += pfm

            worker.algorithm = Shannon()
            li, etp, pfm = worker.evaluation(worker.analyse(data.copy(), freq.copy()), freq.copy())
            result_raw.append(li)
            result_raw.append(pfm)
            avgLength[2] += li
            avgPerformance[2] += pfm

            with open('result_rand_raw.csv', mode="a", newline="") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(result_raw)
        
        result_avg = [case]
        for i in range(3):
            avgLength[i] /= quantity_per_case
            result_avg.append(avgLength[i])
            avgPerformance[i] /= quantity_per_case
            result_avg.append(avgPerformance[i])

        with open('result_rand_avg.csv', mode="a", newline="") as file:
                writer = csv.writer(file, delimiter=',')
                writer.writerow(result_avg)






            # worker.algorithm = Huffman()
            # worker.auto(data.copy(), freq.copy(), huffman_rand, "evo")

    #         result = worker.analyse(data.copy(), freq.copy())
    #         print(result)
    #         avgLength, entropy = worker.evaluation(result, freq)
    #         print(avgLength, entropy)
    #         worker.log('./result.csv', data, freq, result, avgLength, entropy)
        