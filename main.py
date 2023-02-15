import random
import math


def random_list_generator(self, array_size, min_value, max_value):
    pass


def find_max_crossing_subarray(number_array, low: int, mid: int, high: int) -> tuple:
    left_sum = right_sum = -math.inf
    current_left_sum = current_right_sum = 0

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


class MaxSubarray:

    # Initialize array list.
    def __init__(self, number_array: list):
        self.number_array = number_array
        # low and high indexes for the array
        self.low_index = 0
        self.high_index = len(number_array) - 1

        self.left_max = ()
        self.right_max = ()
        self.cross_max = ()

    def find_maximum_subarray(self, number_array: list, low, high) -> tuple:
        # Bring error if array is empty
        if len(number_array) <= 0:
            return "Not enough elements to compare"
        else:
            if high == low:
                return low, high, number_array[low]
            else:
                mid = (low + high) // 2

                # left_low, left_high, left_sum = self.find_maximum_subarray(self, number_array, low, mid)
                # right_low, right_high, right_sum = self.find_maximum_subarray(self, number_array, mid + 1, high)
                # cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(self, number_array, low, mid, high)
                left_low, left_high, left_sum = self.find_maximum_subarray(number_array, low, mid)
                right_low, right_high, right_sum = self.find_maximum_subarray(number_array, mid + 1, high)
                cross_low, cross_high, cross_sum = find_max_crossing_subarray(number_array, low, mid, high)

                if left_sum >= right_sum and left_sum >= cross_sum:
                    self.left_max = (left_low, left_high, left_sum)

                    return left_low, left_high, left_sum
                elif right_sum >= left_sum and right_sum >= cross_sum:
                    self.right_max = (right_low, right_high, right_sum)
                    return right_low, right_high, right_sum
                else:
                    self.cross_max = (cross_low, cross_high, cross_sum)
                    return cross_low, cross_high, cross_sum

    def print_array(self, number_array: list):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [80, 120, 97, 60, 55, 102, 101, 54, 109, 64, 96, 69, 114, 110, 51, 56, 73, 72, 73, 67, 68, 54, 62, 82, 95, 94, 88, 69, 113, 62, 90, 96, 63, 55, 50, 88, 52, 107, 87, 112, 80, 74, 116, 101, 104, 50, 88, 95, 71, 110, 74, 91, 69, 110, 84, 103, 119, 74, 111, 94, 57, 83, 52, 107, 62, 92, 91, 69, 95, 73, 118, 79, 97, 86, 120, 97, 58, 103, 112, 70, 120, 86, 90, 85, 113, 76, 107, 105, 55, 84, 73, 84, 89, 69, 107, 108, 68, 61, 75, 64]
   # a = [0, 700, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 700]
   # a = [7,1,5,3,6,4]
    b = []
    for i in range(len(a) - 1):
        b.append(a[i + 1] - a[i])
    print(b)
    answer = MaxSubarray(b)
    answer.find_maximum_subarray(answer.number_array, answer.low_index, answer.high_index)
    print(answer.left_max)
    print(answer.right_max)
    print(answer.cross_max)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
