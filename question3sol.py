# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:21:16 2019

@author: Shan-CHAUDHARY
"""
num_divsible_5_7=[]
for num in range(1500,2701):
    if num%7==0 and num%5==0:
        num_divsible_5_7.append(num)
print(num_divsible_5_7)