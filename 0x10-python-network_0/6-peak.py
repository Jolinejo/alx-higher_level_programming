#!/usr/bin/python3
"""module for interview q"""


def find_peak(list_of_integers):
    """required func"""
    if list_of_integers == [] or len(list_of_integers) == 0:
        return None
    nums = list_of_integers
    if len(nums) == 1:

        return nums[0]
    if nums[0] > nums[1]:
        return nums[0]
    if nums[len(nums)-1] > nums[len(nums)-2]:
        return nume[len(nums)-1]
    for i in range(1, len(nums)-1):
        if nums[i] >= nums[i-1] and nums[i] >= nums[i+1]:
            return nums[i]
