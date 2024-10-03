# Ejemplo para calcular el area de un triangulo

#Variables de entrada
base  = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#Invocar la funcion
resulado = calcularAreaTriangulo(base,altura)

#Salida
print(f"El area del triangulo cuya base {base} y altura {altura}: {resulado}")

#Funcion con argumento predeterminados

def my_function(country = "Colombia"):
    print("I am from "+country)

#Invocar la funcion
my_function()
my_function("Sweden")

#Argumentos Arbitrarios
def mostrarEstudiantes(*args):
    print("El estudiante es: "+args[2])

#Invocar la funcion
mostrarEstudiantes("Email","Linux","Linus","Bill", "Andres")

#Argumentos palabras clave

def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)

mostrarCarros(carro1= "BMW", carro3= "Ferrari", carro2= "Ford")

# Argumento arbitrario **kwargs
def mostrarClientes(**kwargs):
    print("Su apellido es: " + kwargs["telefono"])

mostrarClientes(nombre = "Tobias", apellido = "Refsnes", direccion = "12345" , telefono = "3127564322")

#Declaracion de paso
def miFuncion():
    pass

#Funciones Integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#Ejemplo funcion pow
num1 = pow(7,4)
print(num1)

#Modulo de matematica
import math
num2 = math.sqrt(34)
print(num2)

#Funcion math.Ceil (redondea hacia arriba)

import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)
print(num3)
print(num4)