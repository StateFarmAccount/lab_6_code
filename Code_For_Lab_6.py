# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:08:35 2023

@author: Kaylu
"""
def Decode(data):
    Ddata = ''
    num = 0
    for i in data:
        if i.isdigit():
            num = int(i) - 3 
            if num < 0:
                num +=10
            Ddata += str(num)
    return Ddata
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
def Menu():
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
        elif select == 2:
            print(f'The encoded password is {storedv}, and the original password is {Decode(storedv)}.')
            

def Main():
    Menu()


if __name__ == "__main__":
    pass
    Main()
    


        
