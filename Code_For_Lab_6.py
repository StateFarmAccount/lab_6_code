# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:08:35 2023

@author: Kaylu
"""
def Encode(data):
    Edata = ''
    num = 0
    for i in data:
        if i.isdigit():
            num = int(i) + 3 
            if num >= 10:
                num %= 10
            Edata += str(num)
    return Edata

def Decode(data):  # decodes encoded password by moving values down 3 digits
    decoded_password = ""
    for digit in data:
        decode = str((int(digit) - 3) % 10)  # shifts each digit down by 3
        decoded_password += decode
    return decoded_password

def Menu():  # shows menu
    storedv = 0 
    while True:
        print('Menu\n''-------------\n')
        select = int(input('1. Encode\n'
                       '2. Decode\n'
                       '3. Quit\n'
                       'Please enter an option:'))
        if select == 3:
            break
        if select == 1:
            value = input(f'Please enter your password to encode:')
            storedv = Encode(value)
            print('Your password has been encoded and stored!')
        elif select == 2:  #decodes password
	    print(f'The encoded password is {storedv}, and the original password is {Decode(storedv)}.')  # shows encoded password and original password (decoded  password)

def Main():
    Menu()


if __name__ == "__main__":
    pass
    Main()
    


        
