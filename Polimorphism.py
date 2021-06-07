class Person:
    def __init__(self, name):
        self.name = name

    def get_moving(self):
        print("I'm walking")


class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print("I'm in my bicicle")

def main():
    person = Person("David")
    person.get_moving()

    cyclist = Cyclist("Peter")
    cyclist.get_moving()

if __name__ == '__main__':
    main()
