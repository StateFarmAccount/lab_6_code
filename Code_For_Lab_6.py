# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:08:35 2023

@author: Kaylu
"""
def Decode(data):
    Ddata = ''
    for i in data:
        if i.isdigit():
            Ddata += str(int(i)-3)
    return Ddata
def Encode(data):
    Edata = ''
    for i in data:
        if i.isdigit():
            Edata += str(int(i)+3)
    return Edata
def Menu():
    stored_value = 0
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
            stored_value = Encode(value)
            print('Your password has been encoded and stored!')
        elif select == 2:
            print(f'The encoded password is {stored_value}, and the original password is {Decode(stored_value)}.')
            

def Main():
    Menu()


if __name__ == "__main__":
    pass
    Main()
    


        
