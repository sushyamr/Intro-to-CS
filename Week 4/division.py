# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:41:08 2018

@author: sushy
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item/denom
    except ZeroDivisionError:
        return 0




