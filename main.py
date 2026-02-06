import json
from pathlib import Path
from student import Student



# A function to load students from the dictionary
def loadStudents():

    file_path = Path('./database.json')

    if file_path.exists() and file_path.stat().st_size >1:
        #Read from file and parse JSON
        with open("database.json", 'r') as f:
        #Deserealize the data  
            data = json.load(f)

        return data
    
#This function only list the users with state is True  
def listAllStudents(): 
        with open("database.json", 'r') as f:
        #Deserealize the data  
            data = json.load(f)
        for studentid, studentData in data.items():
            if studentData["state"] == True:
                print(f"StudentID: {studentid}, studentData: {studentData}")


#Function to create a Database
def createDatabase(): 
    #Create a file 
    with open("database.json", "x") as f:
        pass



# A function to save students in to the dictionary
def saveStudent(studentCatalog):

    # json.dumps() converts a Python object into a JSON-formatted string
    json_str = json.dumps(studentCatalog, indent=4)

    #Create the json file 
    with open("database.json", 'w') as f:
        f.write(json_str)    


#A function to create a menu
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
            return option
        else:
            print("Opcion invalida")
            break


def updateUser(studentCatalog,id): 
    
    #Searh the user if the user state is true
    userSearched = studentCatalog[id]

    if userSearched['state'] == False:
        print("You don't have permision to update")
    else:
        print("This is the information of the user")
        print(userSearched)
        print("\n ")

        print("Update the infromation do you want ")
        name = input("Introduzca el nombre del estudiante: ")
        age =  input("Introduzca el Age: ")
        rol = input("Introduzca el Rol: ")
        average = input("Introduzca el Average: ")

        if name != '':
            userSearched['name'] =name
        
        if age != '':
            userSearched['age'] =int(age)

        if rol != '': 
            userSearched['rol'] =rol

        if average != '':
            userSearched['average'] =int(average)
        
        userUpdated = userSearched
        print(userUpdated)

        studentCatalog[id] = userUpdated

        return studentCatalog

def deleteUser(studentCatalog, id):
    #Search de user by its id in the dictionary
    user = studentCatalog[id]
    user['state'] = False
    studentCatalog[id] = user

    return studentCatalog




#A function to create a student
def createStudent(studentCatalog):
    id = str(len(studentCatalog))
    name = input("Introduzca el nombre del estudiante: ")
    age =  int(input("Introduzca el Age: "))
    rol = input("Introduzca el Rol: ")
    average =  int(input("Introduzca el Average: "))

    #Create user
    newStudent = Student(name, age, rol, True, average)
    #Convert the object into a dictionary with the property .__dict__
    dictionaryStudent = newStudent.__dict__
    #Assing the  dictionary  in the dictionary studentCataLog
    studentCatalog[id] = dictionaryStudent

    return studentCatalog


# A function that its papel is support the actions of student in the system
def studentActions(studentCatalog, option):
    
    if option == 1: 
       createdStudent = createStudent(studentCatalog)
       saveStudent(createdStudent)
    elif(option ==2): #Pendenting to update a user
       id =(input("Write the id of the user \n"))
       userUpdate =updateUser(studentCatalog, id)
       saveStudent(userUpdate)
    elif( option == 3 ): #Delete a user
        id =(input("Write the id of the user do you want to delete \n"))
        userEliminated = deleteUser(studentCatalog, id)
        saveStudent(userEliminated)
    elif(option == 4): #This function list only the user's state is true
        listAllStudents()




# The functio main of the system
def main (): 

    #Create a new empty dictionary
    studentCatalog = dict()

    file_path = Path('./database.json')

    if file_path.exists() and file_path.stat().st_size >1:

        #Load data from the json file
        studentCatalog= loadStudents()
            
    else: 
        createDatabase()


    while True: 

        opcion = menu()
        if(opcion <= 4):
            studentActions(studentCatalog, opcion)
        elif(opcion >= 5 ):

            print("Cerrando sistema : )")
            break

    
#Funcion para ejecutar el main
if __name__ == "__main__":
   main()



