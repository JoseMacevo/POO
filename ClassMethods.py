class Animal(object):
    @classmethod
    def run(self, km):
        return f"The animal have ran {km} kilometers."


print(Animal.run(12))
