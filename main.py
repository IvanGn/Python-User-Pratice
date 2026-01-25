import json 
from student import Student

#Create a new empty dictionary
studentCatalog = dict()


def loadStudents():
    
    #Read from file and parse JSON
    with open("database.json", 'r') as f:
        #Deserealize 
        data = json.load(f)
    
    return data   

def saveStudent(studentCatalog):

    json_str = json.dumps(studentCatalog, indent=4)

    #Create the json file 
    with open("database.json", 'w') as f:
        f.write(json_str)    

def menu():
    while(True):

        print("\n")
        print("Bienvenido al sistema")
        print("¿ Que deseas hacer ? ")
        print(".1 Registrar un usuario")
        print(".2 Actualizar  un usuario")
        print(".3 Eliminar un usuario")
        print(".4 Listar  todos los usuarios")
        print(".5 Salir del sistema")
        print("\n")

        try:
            option = int (input("Seleccione una opcion: "))
        
        except Exception as e: 
            print("Debes ingresar un numero", e)
            continue

        if option <=4:
            return option
        elif option == 5 :
            print("Saliendo del programa :) ")
            return None
        else:
            print("Opcion invalida")
            break





def createStudent(studentCatalog):
    id = str(len(studentCatalog))
    name = input("Introduzca el nombre del estudiante: ")
    age =  int(input("Introduzca el Age: "))
    rol = input("Introduzca el Rol: ")
    average =  int(input("Introduzca el Average: "))

    #Create user
    newStudent = Student(name, age, rol, True, average)
    #Convert the object into a dictionary
    dictionaryStudent = newStudent.__dict__
    #Assing the  dictionary  in the dictionary studentCataLog
    studentCatalog[id] = dictionaryStudent



    return studentCatalog



def studentActions(studentCatalog, option):
    
    if option == 1: 
       createdStudent = createStudent(studentCatalog)
       saveStudent(createdStudent)
    elif(option ==2): 
        pass
    elif(option == 4):
        print(loadStudents())





def main (): 

    #Load data from the file
    studentCatalog= loadStudents()

    while True: 

        opcion = menu()
        if(opcion <= 4):
            studentActions(studentCatalog, opcion)
        else:
            break

    

if __name__ == "__main__":
   main()



