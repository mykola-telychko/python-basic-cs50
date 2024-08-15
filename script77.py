class Student:
    def __init__(self, name, house, religion):
        if not name: 
            raise ValueError("Missing name")
        if house not in ["Ukraine", "Greece", "Bulgaria"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house
        self.religion = religion

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def getReligion(self):
        match self.religion:
            case "Orthodox":
                return "_+"
            case "Islam":
                return "*"
            case "Judaism":
                return "="
            case _: 
                return "ateism"


def main(): 
    student = get_student()
    print(student.getReligion())
    # print(f"{student.name} from {student.house}")

def get_student(): 
    name = input("Name: ")
    house = input("House: ")
    religion = input("Religion: ")
    return Student(name, house, religion)

if __name__ == "__main__": 
    main()