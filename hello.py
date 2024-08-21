#!/usr/share/python
# python program to demonstrate hello world in OOP style

class Hello:

    def __init__(self, name, age)->None:
        self._name = name
        self._age = age

    def getName(self)->str:
        return self._name

    def setName(self,name):
        self._name = name

    def getAge(self)->int:
        return self._age

    def setAge(self, age):
        try:
            self._age = int(age)
        except (ValueError) as e:
            print(e)

    def __repr__(self)->None:
        return f'Hello {self._name}, happy pythoning at {self._age} years old!'


if __name__ == "__main__":

    hello = Hello("Mulyo Santoso", 43)
    print(hello.__repr__())

    myName = input("Enter your name: ")
    hello.setName(myName)

    myAge = input("Enter your age: ")
    hello.setAge(myAge)

    print(hello.__repr__())

    
