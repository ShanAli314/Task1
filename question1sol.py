# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:00:59 2019

@author: Shan-CHAUDHARY
"""

n_value=(input("Enter the value of n: ")) #input for n

#By Print Method
print(int(n_value)+int(n_value*2)+int(n_value*3))


#Accumalative Pattern
sum=0
for num in range(1,4):
    sum=sum+int(n_value*num)
print(sum)    