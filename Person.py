class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def greet (self):
        print(f"Hello {self.name}, you are a {self.role}")


user = Person("CJ", "Student")
user.greet()