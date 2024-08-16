class Wizard: 
    def __init__(self, name): 
        if not name: 
            raise ValueError("Missing name")
        self.name = name 
    ... 


class Student(Wizard): 
    def __init__(self, name, house): 
        super().__init__(name)
        # self.name = name 
        self.house = house 

    ...

class Professor(Wizard): 
    def __init__(self, name, subject): 
        super().__init__(name)
        # self.name = name 
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
student = Professor("Severus", "Def Against the Dark Arts")