# from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import math
import csv

from Algorithm import *


class Worker():
    def __init__(self, algorithm = None) -> None:
        self.algorithm = algorithm if algorithm else None

    # calculate the encoding result 
    def analyse(self, data: List, freq: List) -> None:
        result = self.algorithm.execute(data, freq)
        return result

    # calculate average length and entropy and performance
    def evaluation(self, encoded: List, probability: List):
        avgLength = 0.0
        entropy = 0.0
        for idx in range(len(encoded)):
            avgLength += len(encoded[idx]) * probability[idx]
            entropy -= probability[idx] * (math.log(probability[idx], 2))
        performance = round(100 * entropy / avgLength, 2)
        entropy = round(entropy, 2)
        avgLength = round(avgLength, 2)
        return avgLength, entropy, performance

    def log(self, path, data, freq, result, avgLength, entropy, performance):
        with open(path, mode="a", newline="") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(freq)
            result.append(avgLength)
            result.append(entropy)
            result.append(performance)
            writer.writerow(result)

    # def log_evoluation_only(self, path, avgLength, entropy):
    #     result = []
    #     with open(path, mode="a", newline="") as file:
    #         writer = csv.writer(file, delimiter=',')
    #         result.append(avgLength)
    #         result.append(entropy)
    #         writer.writerow(result)


    # def auto(self, data, freq, path, mode):
    #     result = self.analyse(data, freq)
    #     avgLength, entropy = self.evaluation(result, freq)
    #     if(mode == "all"):
    #         self.log(path, data, freq, result, avgLength, entropy)
    #     if(mode == "evo"):
    #         self.log_evoluation_only(path, avgLength, entropy)
    
    def auto_console(self, data, freq):
        # result = self.analyse(data, freq)
        # print(result)
        # avgLength, entropy, performance = self.evaluation(result, freq)
        # print(avgLength, entropy, performance)
        # self.log('./result.csv', data, freq, result, avgLength, entropy, performance)

        # result = self.analyse(data, freq)
        # print("\tSymbol\tProbability\tCodeword")
        # for i in range(len(data)):
        #     print("\n\t",data[i],"\t",freq[i],"\t\t",result[i])
        # avgLength, entropy, performance = self.evaluation(result, freq)
        # print("\naverage length(Ltb): ",avgLength, "\nEntropy of source(H(x)): " ,entropy,"\nCoding efficiency(Kt%): ", performance,"\n\n")
        # self.log('./result.csv', data, freq, result, avgLength, entropy, performance)

        result = self.analyse(data, freq)
        print("\txi\tP(xi)\t\tCodeword\t\tli\tH(xi)\t\tP(xi).li")
        avgLength, entropy, performance = self.evaluation(result, freq)
        for i in range(len(data)):
            print("\n\t",data[i],"\t",freq[i],"\t\t",result[i], "\t\t\t", len(result[i]), "\t", entropy, "\t\t", round(freq[i]*len(result[i]), 2))
        print("\naverage length(Ltb): ",avgLength, "\nEntropy of source(H(x)): " ,entropy,"\nCoding efficiency(Kt%): ", performance,"\n\n")
        self.log('./result.csv', data, freq, result, avgLength, entropy, performance)