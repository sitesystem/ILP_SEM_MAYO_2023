# Operaciones Matemáticas usando los operadores

# Importar una librería o biblioteca para usar funciones o constantes matemáticas
import math # Matemáticas

# ENTRADA DE DATOS
# Declarar o o crear las variables
número_1 = float(input("Escribe el 1er número: ")) # Convertir un tipo de dato en otro tipo de dato (CASTEO)
número_2 = float(input('Escribe el 2do número: '))

# Declarar constante
PI = 3.1416

# PROCESOS (Cálculos u operaciones Matemáticas y/o Lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
mult = número_1 * número_2
div = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2) # Los valores o elemntos que están dentro de los paréntesis se llaman parámetros o argumentos
cuadrado = número_1 ** 2
cubo = pow(número_2, 3)

raíz_cuadrada_1 = math.sqrt(9)
raíz_cuadrada_2 = pow(9, 1/2)
raíz_cúbica = pow(27, 1/3)

módulo_residuo = número_1 % número_2

# SALIDA DE DATOS
print("La constante PI es =", PI)
print("La suma es =", round(suma, 2))
print('La resta es =', round(resta, 2))
print(mult)
print(div)
print("El módulo o residuo es =", módulo_residuo)

