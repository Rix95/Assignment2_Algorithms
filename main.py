import random
import math
from tabulate import tabulate
import numpy as np

print(
    "================================================================================================================")
print("                                 Developer Ricardo Elizondo")
print(
    "================================================================================================================")
print("                              School name: Texas A&M San Antonio")
print("                                          Algorithms")
print("                                          Assignment 2")
print("                                          Submitted  February 16, 2023")
print("                                 Semester/Year: Spring 2023")
print(
    "================================================================================================================")
print("")


print("This program calculates the Max profit using the max contiguous subarray algorithm, a class was implemented\n"
      "to address assignment specific requirements, the core functions are outside of the class scope. \n"
      "A tester function has been added to testcase the assignment. Certain libraries were used\n"
      "to improve assignment presentation and facilate certain tasks.\n"
      "")


# find maximum subarray implemented from pseudocode given.
def find_maximum_subarray(number_array: list, low, high):
    # Bring error if array is empty
    if len(number_array) <= 0:
        return 0, 0, 0
    else:
        if high == low:
            return low, high, number_array[low]
        else:
            mid = (low + high) // 2

            left_low, left_high, left_sum = find_maximum_subarray(number_array, low, mid)
            right_low, right_high, right_sum = find_maximum_subarray(number_array, mid + 1, high)
            cross_low, cross_high, cross_sum = find_max_crossing_subarray(number_array, low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            else:
                return cross_low, cross_high, cross_sum


# find max crossing subarray implemented from pseudocode given.
def find_max_crossing_subarray(number_array, low: int, mid: int, high: int):
    left_sum = right_sum = -math.inf
    current_left_sum = current_right_sum = max_left_index = max_right_index = 0

    for i in range(mid, low - 1, -1):
        current_left_sum = current_left_sum + number_array[i]
        if current_left_sum > left_sum:
            left_sum = current_left_sum
            max_left_index = i

    for j in range(mid + 1, high + 1):
        current_right_sum = current_right_sum + number_array[j]
        if current_right_sum > right_sum:
            right_sum = current_right_sum
            max_right_index = j

    return max_left_index, max_right_index, left_sum + right_sum


# class to hold values of Max profit and also print table. recursion side is out of scope.
class MaxProfit:

    # Initialize list.
    def __init__(self, price_array: list):
        # check for list integrity
        self.valid_list = True if len(price_array) > 1 else False

        self.price_array = price_array

        self.daily_change_list = []  # array to store daily changes
        self.get_daily_changes()
        # low and high indexes for the array
        self.low_index = 0
        self.high_index = len(self.daily_change_list) - 1
        self.mid_index = (self.low_index + self.high_index) // 2

        # local max indexes including best choice
        self.left_max = ()
        self.right_max = ()
        self.cross_max = ()
        self.best_choice = (0, 0, 0)

        self.find_maximum_values()

    #  get all price changes from price array.
    def get_daily_changes(self):
        for idx in range(len(self.price_array) - 1):
            self.daily_change_list.append(self.price_array[idx + 1] - self.price_array[idx])
        return

    #  find maximum values for left, right and cross, calls to recursive outer function.
    def find_maximum_values(self):
        # Bring error if array is empty
        if len(self.price_array) <= 0:
            return
        else:
            self.left_max = find_maximum_subarray(self.daily_change_list, self.low_index, self.mid_index)
            self.right_max = find_maximum_subarray(self.daily_change_list, self.mid_index + 1, self.high_index)
            self.cross_max = find_max_crossing_subarray(self.daily_change_list, self.low_index, self.mid_index,
                                                        self.high_index)

            #  sorts tuples to select best choice available, store in variable
            tuple_list = sorted([self.left_max, self.right_max, self.cross_max], key=lambda x: x[2], reverse=True)
            self.best_choice = tuple_list[0]
            return

    #  print table with n elements in each column, tabulate library used to enhance displaying purposes.
    def get_max_profit(self):
        if self.valid_list:
            self.find_maximum_values()
            self.print_list()
            if self.best_choice[2] <= 0:
                print("There is no best day to buy and sell :(.")
            else:
                print("\nThe local left indexes are: " + str(self.left_max))
                print("The local right indexes are: " + str(self.right_max))
                print("The local cross indexes are: " + str(self.cross_max) + "\n")
                print("The best day to buy is day " + str(self.best_choice[0] + 1)
                      + ", the best day to sell is day " + str(self.best_choice[1])
                      + ". Total profit: " + str(self.best_choice[2]) + ".")

        else:
            print("Not enough elements in list.")

    def print_list(self):
        if len(self.price_array) <= 0:
            print("Not enough elements to return")
            return

        COLUMN_MAX_ELEMENTS = 25  # number of columns per line.
        current_index = 0
        daily_change_list_copy = [""] + self.daily_change_list.copy()  # format with blank space for table

        def print_array_with_column_format(low_index, max_index):
            table = [["Price"] + self.price_array[low_index:max_index], ["Change"]
                     + daily_change_list_copy[low_index:max_index]]
            headers = ["Day"] + list(np.arange(low_index + 1, max_index + 1))

            print(tabulate(table, headers, tablefmt="simple_grid"))

        while current_index < len(self.price_array):
            max_idx = current_index + COLUMN_MAX_ELEMENTS
            if max_idx > len(self.price_array):
                max_idx = len(self.price_array)
            print_array_with_column_format(current_index, max_idx)
            current_index += COLUMN_MAX_ELEMENTS


# function used to test and compare main program, output might differ in certain edge cases.
def test_subarray_sum(array):
    maxint = math.inf
    transformed_array = []
    for i in range(len(array) - 1):
        transformed_array.append(array[i + 1] - array[i])

    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, len(transformed_array)):
        max_ending_here = max_ending_here + transformed_array[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


# generate new random list with assigned values
def random_list_generator(list_size, min_value, max_value):
    random_generated_list = []
    for i in range(0, list_size):
        n = random.randint(min_value, max_value)
        random_generated_list.append(n)

    #  print(random_generated_list)
    return random_generated_list


def main():
    # sample test cases, edge cases included.
    a = [80, 120, 97, 60, 55, 102, 101, 54, 109, 64, 96, 69, 114, 110, 51, 56, 73, 72, 73, 67, 68, 54, 62, 82, 95, 94,
         88, 69, 113, 62, 90, 96, 63, 55, 50, 88, 52, 107, 87, 112, 80, 74, 116, 101, 104, 50, 88, 95, 71, 110, 74, 91,
         69, 110, 84, 103, 119, 74, 111, 94, 57, 83, 52, 107, 62, 92, 91, 69, 95, 73, 118, 79, 97, 86, 120, 97, 58, 103,
         112, 70, 120, 86, 90, 85, 113, 76, 107, 105, 55, 84, 73, 84, 89, 69, 107, 108, 68, 61, 75, 64]
    b = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    c = [7]
    d = []
    e = random_list_generator(100, 50, 120)
    f = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

    tests = []

    testcase_a = MaxProfit(a)
    testcase_b = MaxProfit(b)
    testcase_c = MaxProfit(c)
    testcase_d = MaxProfit(d)
    testcase_e = MaxProfit(e)
    testcase_f = MaxProfit(f)

    # extra function added to compare algorithm implemented.
    tests.append({'input': testcase_a.best_choice[2], 'output': test_subarray_sum(a)})
    tests.append({'input': testcase_b.best_choice[2], 'output': test_subarray_sum(b)})
    tests.append({'input': testcase_c.best_choice[2], 'output': 0})  # only one day, so 0.
    tests.append({'input': testcase_d.best_choice[2], 'output': 0})  # max_subarray_sum takes negative values, so 0.
    tests.append({'input': testcase_e.best_choice[2], 'output': test_subarray_sum(e)})
    tests.append({'input': testcase_f.best_choice[2], 'output': test_subarray_sum(f)})

    print("Test cases using happy and edge cases.\n")
    for i in range(len(tests)):
        print(f'Test {i + 1} Pass:',
              tests[i]['input'] == tests[i]['output'])
    print("///////////////////////////////////////////////////////\n")

    # max profit variable can be changed to selected desired test case, choose e for random generated input
    custom_test_case = MaxProfit(e)
    custom_test_case.get_max_profit()


if __name__ == '__main__':
    main()
