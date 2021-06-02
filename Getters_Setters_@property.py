#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class Dogs(object):  # Declaramos la clase principal.
    def __init__(self, name, wheight):  # Definición de los parámetros.
        self.__name = name  # Atributos privados y por lo tanto ocultos.
        self.__wheight = wheight

    @property
    def name(self):  # Definimos el método para obtener el nombre.
        """Method documentation, name, etc..."""
        return self.__name  # Aquí simplemente estamos devolviendo el atributo privado.

    # Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
    # Ahora utilizaremos setter y deleter para modificarlos.

    @name.setter  # Propiedad SETTER
    def name(self, new):
        print("Changing name ----->----->------->")
        self.__name = new
        print(f"The name have been modificated by {self.__name} ")

    @name.deleter  # Propiedad DELETER.
    def name(self):
        print("Erasing name -->--->----->")
        del self.__name

    @property
    def wheight(self):  # Definimos el método para obtener el peso automáticamente GETTER.
        return self.__wheight  # Aquí simplemente estamos devolviendo el atributo privado.

    @wheight.setter
    def wheight(self, neweight):
        self.__wheight = neweight
        print(f"The new wheight is {self.__wheight}")

    @wheight.deleter  # Propiedad DELETER
    def wheight(self):
        print("Erasing wheight.....")
        del self.__wheight


# INSTANCIAMOS.

Tomas = Dogs('Tom', 27)
print(Tomas.name)  # Impresión del nombre de Tomas. Se hace a través de getter
# El cual en este caso está a continuación de property, lo toma como el primer método.

Tomas.name = 'Tomasito'
print(Tomas.name)
Tomas.wheight = 28
del Tomas.name
