nombre = input("Ingrese el nombre: ")

while nombre == "":
    print("El nombre no puede estar vacío")
    nombre = input("Ingrese el nombre: ")

nota1 = float(input("Ingrese la nota 1 (0-100): "))
while nota1 < 0 or nota1 > 100:
    print("Nota inválida")
    nota1 = float(input("Ingrese la nota 1 (0-100): "))

nota2 = float(input("Ingrese la nota 2 (0-100): "))
while nota2 < 0 or nota2 > 100:
    print("Nota inválida")
    nota2 = float(input("Ingrese la nota 2 (0-100): "))

nota3 = float(input("Ingrese la nota 3 (0-100): "))
while nota3 < 0 or nota3 > 100:
    print("Nota inválida")
    nota3 = float(input("Ingrese la nota 3 (0-100): "))

promedio = (nota1 + nota2 + nota3) / 3

print("Estudiante:", nombre)
print("Promedio:", promedio)
