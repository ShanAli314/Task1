# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 07:22:26 2019

@author: Shan-CHAUDHARY
"""
#64-68-72-78-84
#97-101-105-111-117
#list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
input_string=input("Enter a string :")
digits=0
letters=0
for i in range(len(input_string)):
    char_temp=ord(input_string[i])
    if char_temp > 47 and char_temp<58:
        digits+=1
    elif char_temp > 64 and char_temp<90:
        letters+=1
    elif char_temp > 96 and char_temp<122:
        letters+=1
print("Digits: ".format(digits))
print("Letters: ".format(letters))
