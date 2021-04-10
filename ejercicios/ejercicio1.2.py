print("INGRESAR VALORES DE PERSONA")

nombre = input("INGRESE EL NOMBRE:  ")
edad = int(input("INGRESE LA EDAD:  "))
teledono = int(input("INGRESE TELEFONO: "))

persona = [nombre, edad, teledono]

print("LOS DATOS SON: " + persona[0], persona[1], persona[2])