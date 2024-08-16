# Hello World in OOP Style

class Hello:
    _name ="Mulyo Santoso"
    _age = 43

    def __init__(self, name=_name, age=_age) -> None:
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def __repr__(self) -> str:
        return f"Hello {self.name}, now you are {self.age} years old." 
    
if __name__=="__main__":

    hello = Hello()

    print(hello.__repr__())