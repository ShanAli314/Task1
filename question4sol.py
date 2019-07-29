# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:24:49 2019

@author: Shan-CHAUDHARY
"""
#65-69-73-79-85
#97-101-105-111-117
cont = True
alpha_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
consonant_list=[66,67,68,70,71,72,74,75,76,77,78,80,81,82,83,84,86,87,88,89,90,98,99,100,102,103,104,106,107,108,109,110,112,113,114,115,116,118,119,120,121]
while cont:
    char=input("Enter Alphabet or others to exit: ")
    if char in alpha_list:
        char=ord(char)
        if(char==65 or char==69 or char==73 or char==79 or char==85 or char==97 or char==101 or char==105 or char==111 or char==117):
            print("It is vowel")
        elif char in consonant_list:
                print("It is consonant")
    else:
        cont = False
   