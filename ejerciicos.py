# 1.- Bucle for de Python:
numeros = [10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]

# Variables para almacenar las sumas
suma_pares = 0
suma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        # Si el número es par, agregarlo a la suma de pares
        suma_pares += numero
    else:
        # Si el número es impar, agregarlo a la suma de impares
        suma_impares += numero

print(f'Suma de números pares: {suma_pares}')
print(f'Suma de números impares: {suma_impares}')



# 2.- Función de Python llamada suma: toma 3 argumentos y devuelve la suma de los 3.
def suma(a, b, c):
    return a + b + c

# Ejemplo deL uso de la función suma
resultado = suma(15, 34, 28)
print(f'La suma de 15, 34 y 28 es: {resultado}')


#3.- Función lambda de Python con la misma funcionalidad de la funcion suma:
suma = lambda a, b, c: a + b + c

resultado = suma(15, 34, 28)
print(f'La suma de 15, 34 y 28 es: {resultado}')



# 4.-Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista:
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']


#Variable para almacenar si hay coincidencia

coincidencia = False

for n in lista_nombre:
    if n == nombre:
        coincidencia = True
        break

# imprimir el resultado
if coincidencia:
    print(f'El nombre {nombre} coincide con un nombre de la lista.') 
else:
    print(f'El nombre {nombre} no coincide con ningún nombre de la lista.')