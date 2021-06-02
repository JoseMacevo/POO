# -*-coding: utf-8 -*-
class MyDecorator(object):
    def __init__(self, func):
        print("I´ve make the class")
        func()

    def __call__(self):
        print("I´m a class named through a __call__ method. ")


@MyDecorator
def speak():
    print("Hi...I´m speak function...")

#John = MyDecorator(speak)  # Instanciamos y llamamos a la función speak brindándola como
# argumento