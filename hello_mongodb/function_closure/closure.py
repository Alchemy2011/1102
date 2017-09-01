# -*- coding: utf-8 -*-


def adder(x):
    def wrapper(y):
        return x + y

    return wrapper


adder5 = adder(5)
print(adder5(10))
print(adder5(6))
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents)
"""4
def print_msg():
    msg = "zen of python"

    def printer():
        print(msg)

    return printer


another = print_msg()
another()
"""
"""3
def print_msg():
    msg = 'zen of python'

    def printer():
        print(msg)

    printer()


print_msg()
"""
"""2
num = 10


def foo():
    print(num)
"""
"""1
def foo():
    num = 10
    print(num)
"""
