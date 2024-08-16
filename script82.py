import random

class Hat: 
   
    houses = ["Gryff", "Huff", "Rave", "Slyth"]
    
    @classmethod
    def sort(cls, name): 
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
# old
# hat = Hat()
# hat.sort("Harry")