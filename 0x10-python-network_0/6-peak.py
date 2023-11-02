#!/usr/bin/python3
"""module for interview q"""


def find_peak(list_of_integers):
    """required func"""
    if list_of_integers == [] or len(list_of_integers) == 0:
        return None
    nums = list_of_integers
    left = 0
    r = len(nums) - 1
    while (left < r):
        mid = (l + r) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            r = mid
    return nums[left]
