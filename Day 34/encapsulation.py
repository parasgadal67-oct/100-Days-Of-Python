#Creating Student Report Card system using O.O.P.
class Students:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks
    
    def update_marks(self, new_marks):
        if new_marks >= 0 and new_marks <= 100:
            old_marks = self.__marks
            self.__marks = new_marks
            print(f"{self.name}'s marks updated from {old_marks} to {new_marks} ")
        else:
            print(f"Invalid marks '{new_marks}' . Marks should be between 0 to 100")

student1 = Students("Paras Gadal", 27,  84)
student2 = Students("Ayush", 23, 88)          
print(student2.name)
print(student2.roll_no)            
print(student2.get_marks())
student2.update_marks(99)
student2.update_marks(170)
