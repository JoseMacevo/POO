class Bird(object):
    """
    Class to create birds...
    Another stupid example.
    """
    def __init__(self):
        pass

    def speak(self, color):
        return f"I´m a {color} bird"

    @staticmethod
    def function_fly_bird(have_wings, kms):
        """Conditional"""
        if have_wings:
            return f"The bird flew away {kms} kilometers."
        else:
            return f"This bird can´t fly"


print(Bird.function_fly_bird(True, 1))
