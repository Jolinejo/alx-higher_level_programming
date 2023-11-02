#!/usr/bin/python3
"""module for interview q"""


def find_peak(list_of_integers):
    """required func"""
    if list_of_integers == [] or len(list_of_integers) == 0:
        return None
    nums = list_of_integers
    l = 0
    r = len(nums) - 1
    while (l < r):
        mid = (l + r) // 2
        if nums[mid] < nums[mid+1]:
            l = mid + 1
        else:
            r = mid
    return nums[l]
