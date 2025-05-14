#!/usr/bin/env python3

# lib/list_comprehension.py

def return_evens(nums):
    return [num for num in nums if num % 2 == 0]

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]