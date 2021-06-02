class Dogs(object):
    """
    Dogs class to create objetcts
    type dogs in this stupid example.
    """
    neck_lace = True  # --> Class Variable or Static Variable

    def __init__(self, health, hunger):
        self.__health = health   # --> Instance Variables. (protected variables).
        self.__hunger = hunger   # --> Instance Variables. (protected variables).


print(Dogs.neck_lace)
Teo = Dogs(100, 10)
print(Teo._Dogs__hunger)  # --> How to access protected variables.
