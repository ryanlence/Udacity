# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 23:46:06 2018

@author: rlence
"""


def main():
    name = input('give me your input')

    name = name.lower()

    while True:
        if name == 'fun1':
            return fun1()
        else:
            return fun2()


def fun1():
    print('hello')


def fun2():
    print('bye')


main()