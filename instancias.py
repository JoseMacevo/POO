class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self, other_person):
        return f"Hi {other_person.name}, my name is {self.name}"


David = Person('David', 35)
Erika = Person('Erika', 32)

print(David.greet(Erika))
print(isinstance(David, Person))
