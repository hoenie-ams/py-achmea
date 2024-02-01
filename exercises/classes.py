

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"hello from {self.name}")


class Student(Person):
    def learn(self, language):
        print(f"{self.name} is learning {language}")


person = Person("John", 42)
print(person.name)
print(person.age)
person.say_hello()

student = Student("Jane", 32)
student.learn("Python")
