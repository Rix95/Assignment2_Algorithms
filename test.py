from math import inf

maxint = inf


def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [80, 120, 97, 60, 55, 102, 101, 54, 109, 64, 96, 69, 114, 110, 51, 56, 73, 72, 73, 67, 68, 54, 62, 82, 95, 94, 88, 69, 113, 62, 90, 96, 63, 55, 50, 88, 52, 107, 87, 112, 80, 74, 116, 101, 104, 50, 88, 95, 71, 110, 74, 91, 69, 110, 84, 103, 119, 74, 111, 94, 57, 83, 52, 107, 62, 92, 91, 69, 95, 73, 118, 79, 97, 86, 120, 97, 58, 103, 112, 70, 120, 86, 90, 85, 113, 76, 107, 105, 55, 84, 73, 84, 89, 69, 107, 108, 68, 61, 75, 64]
#a = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
b = []

for i in range(len(a) - 1):
    b.append(a[i + 1] - a[i])

print(b)

print("Maximum contiguous sum is", maxSubArraySum(b, len(b)))