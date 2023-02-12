"""
    Se necesita crear un codigo en python con las siguientes caracteristica
    nombre del usuario 
    apellido del usuario 
    edad del usuario 
    sexo del usuario 
    telefono del usuario 
    gmail del usuario 
    ciudad del usuario 
    
    y despues mostrar por pantalla los datos 
    
    nombreUsuario: str: tipo de datos string
    apellidoUsuario: str: tipo de datos string
    edadUsuario: int: tipo de datos int
    sexoUsuario: str: tipo de datos string 
    telefonoUsuario: int: tipo de datos int 
    gmailUsuario: str: tipo de datos string 
    ciudadUsuario: str: tipo de datos string 
"""

print("Registo de Persona: -----------------")
print("-------------------------------------")

nombreUsuario = input("Ingrese el nombre: ")
apellidoUsuario = input("Ingrese el apellido: ")
edadUsuario = int(input("Ingrese su edad: "))
sexoUsuario = input("Ingrese el sexo (Masculino/Femenino): ")
telefonoUsuario = int(input("Ingrese su telefono: "))
gmailUsuario = input("Ingrese su Gmail: ")
ciudadUsuario = input("Ingrese su Ciudad: ")

print("---------------------------------------")

print("Su nombre es : " +nombreUsuario )
print("Su apellido es: " +apellidoUsuario )
print("Su edad es: " +edadUsuario + " años" )
print("Su sexo es: " +sexoUsuario )
print("Su telefono es: " +telefonoUsuario )
print("Su gmail es: " +gmailUsuario )
print("Su ciudad es: " +ciudadUsuario)

print("----------------------------------------")