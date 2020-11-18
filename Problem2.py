# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5],
# for first 2 * 3 * 4 * 5 = 120, second 3*4*5*1=60, third 4*5*1*2=40, fourth 5*1*2*3=30, last 1*2*3*4=24
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

def product(arr):
    nxt = 1
    size = len(arr)-1
    newarr = []

    for num in range(size): #4
        pass


arr = [1, 2, 3, 4, 5]