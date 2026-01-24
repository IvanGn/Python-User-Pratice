from user import User 

class Student(User): 

    def __init__(self,name="none", age=0, rol="student", state=True, average=0):
        
        #Call the parent class constrcutor
        super().__init__(name, age, rol, state)

        self.average = average

    def showData(self):
        print("Name: " + self.name)
        print(f"Age: " + str(self.age))
        print("Rol: " + self.rol)
        print("Average: " + str(self.average))
        auxState = "Activado" if self.state else "Desactivado"
        print("State: " +  auxState)



    
