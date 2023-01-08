from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from os import system, path
from library import *

from Algorithm import *
from Worker import *


if __name__ == "__main__":
    system("cls")

    # data, freq = input_from_keyboard()
    # print(data)
    # print(freq)

    # data = ["A"] * 6
    # freq = [0.28, 0.22, 0.16, 0.15, 0.14, 0.05]
    # worker = Worker()
    # worker.algorithm = Huffman()
    # worker.auto_console(data, freq)

    print('choose a way to run this program')
    print('1. read data from .csv file')
    print('2. read data from keyboard')
    print('0. exit')
    choice = int(input("your choice: "))
    while(choice != 0 and choice != 1 and choice != 2):
        system("cls")
        print("invalid choice, sudo try again!")
        print('choose a way to run this program')
        print('1. read data from .csv file')
        print('2. read data from keyboard')
        print('0. exit')
        choice = int(input("your choice: "))
    if(choice == 1):
        system("cls")
        print("prepare a file named input.csv in the current directory, then press ENTER to continue!")
        input()
        while(not path.isfile('./input.csv')):
            system("cls")
            print("we cannot find required file, sudo try again, then press ENTER to continue!")
            input()
        data, freq = read_input_csv('./input.csv')
        while(check_valid_probability(freq) != 1):
            system("cls")
            print("sum of probabilities does not equal 1 or a propability equals 0, sudo try again, then press ENTER to continue!")
            input()
            data, freq = read_input_csv('./input.csv')
    elif(choice == 2):
        system("cls")
        data, freq = input_from_keyboard()
        while(check_valid_probability(freq) != 1):
            system("cls")
            print("sum of probabilities does not equal 1 or a propability equals 0, sudo try again")
            data, freq = input_from_keyboard()
    elif(choice == 0):
        pass
    if(choice in [1, 2]):
        result_file = './result.csv'
        worker = Worker()
        print(data)
        worker.algorithm = Fano()
        print("Fano result:")
        worker.auto_console(data.copy(), freq.copy())

        worker.algorithm = Huffman()
        print("Huffman result:")
        worker.auto_console(data.copy(), freq.copy())

        worker.algorithm = Shannon()
        print("Shannon result:")
        worker.auto_console(data.copy(), freq.copy())

        print('result was logged in result.csv file')
        input("press ENTER to finish!")

        
        

    # data, freq = input_from_keyboard()

    # worker = Worker()

    # worker.algorithm = Shannon()
    # # result = worker.analyse(data.copy(), freq.copy())
    # # print(result)
    # # avgLength, entropy = worker.evaluation(result, freq)
    # # print(avgLength, entropy)
    # # worker.log('./result.csv', data, freq, result, avgLength, entropy)
    # worker.auto(data.copy(), freq.copy(), result_file, "all")

    # worker.algorithm = Huffman()
    # worker.auto(data.copy(), freq.copy(), result_file, "all")
    # # result = worker.analyse(data.copy(), freq.copy())
    # # print(result)
    # # avgLength, entropy = worker.evaluation(result, freq)
    # # print(avgLength, entropy)
    # # worker.log('./result.csv', data, freq, result, avgLength, entropy)