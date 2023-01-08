from os import system
import csv

# sort data and freq in decreasing order of freq
def sort_by_freq(data, freq):
    def swap(i, j):
        data[i], data[j] = data[j], data[i]
        freq[i], freq[j] = freq[j], freq[i]
    n = len(freq)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if freq[i - 1] < freq[i]:
                swap(i - 1, i)
                swapped = True

# read data and freq from .csv file and sort them by using sort_by_freq()
def read_input_csv(path):
    with open(path) as input:
        csv_reader = csv.reader(input, delimiter=',')
        line = 0
        for row in csv_reader:
            if(line == 0):
                data = row
                line += 1
            else:
                freq = row
    for i in range(len(freq)): freq[i] = float(freq[i])
    sort_by_freq(data, freq)
    return data, freq

# get input data from keyboard, valid input is required
def input_from_keyboard():
    freq = [0.1, 0.2]
    n_code_word = int(input("number of code words: "))
    data = []
    freq = []
    for i in range(n_code_word):
        data.append(input(f"c[{i}] = "))
        freq.append(float(input(f"p[{i}] = ")))
        while((sum_probability(freq) >= 1 and i < n_code_word - 1) or freq[i] == 0 or (sum_probability(freq) > 1 and i == n_code_word - 1) or (check_valid_probability(freq) == 0 and i == n_code_word - 1)):
            freq[i] = float(input(f"bad input, re-enter: p[{i}] = "))
    # while(check_valid_probability(freq) == 0):
    #     system("cls")
    #     print("sum of probability does not equal 1, sudo try again!")
    #     n_code_word = int(input("number of code words: "))
    #     data = []
    #     freq = []
    #     for i in range(n_code_word):
    #         # data.append(input(f"c[{i}] = "))
    #         freq.append(float(input(f"p[{i}] = ")))
    #         while((sum_probability(freq) >= 1 and i < n_code_word - 1) or freq[i] == 0 or (sum_probability(freq) > 1 and i == n_code_word - 1)):
    #             freq[i] = float(input(f"yeu cau nhap lai: p[{i}] = "))
    return data, freq

def sum_probability(freq):
    sum = 0.0
    for i in range(len(freq)): sum += freq[i]
    return sum

# check sum of probability, return 1 if sum = 1 and 0 if sum != 1
def check_valid_probability(freq):
    sum = 0.0
    for i in range(len(freq)):
        if freq[i] == 0 : return 0
        sum += freq[i]
    sum = round(sum, 4)
    if sum == 1 : return 1
    if sum != 1 : return 0
