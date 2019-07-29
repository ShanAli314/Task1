# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 09:19:21 2019

@author: Shan-CHAUDHARY
"""
num_list=[]
cont=True
while cont:
    try:
        user_input = input ("Enter a number or else to end")
        val = int(user_input)
        num_list.append(val)
    except ValueError:
        cont=False
num_list.remove(min(num_list))
print(min(num_list))