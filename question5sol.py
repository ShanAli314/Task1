# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:03:26 2019

@author: Shan-CHAUDHARY
"""
import math
num_list=[]
cont=True
while cont:
    try:
        user_input = input ("Enter a number or else to end:")
        val = int(user_input)
        num_list.append(val)
    except ValueError:
        cont=False
print(num_list)
print(min(num_list))