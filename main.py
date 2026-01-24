from student import Student


def loadStudents():
    pass


def saveStudent():
    pass



def createStudent(studentCatalog):
    id = str(len(studentCatalog))
    name = input("Introduzca el nombre del estudiante: ")
    age = input("Introduzca el Age: ")
    rol = input("Introduzca el Rol: ")
    average = input("Introduzca el Average: ")

    #Create user
    newStudent = Student(name, age, rol, True, average)
    studentCatalog[id] = newStudent



studentCatalog = dict()



def main (): 
    print("Bienvenido al sistema")
    print("¿ Que deseas hacer ? ")
    print(".1 Registrar usuarios")
    print(".2 Actualizar usuarios")
    print(".3 Eliminar un usuario")
    print(".4 Listar usuarios")
    #option = int (input())
    createStudent(studentCatalog)
    studentCatalog["0"].showData()


if __name__ == "__main__":
   main()


