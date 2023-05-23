edad = int(input("Edad: "))

# SINTAXIS CONDICIONALES ESTRUCTUTURAS DE CONTROL DE FLUJO: SELECCIÓN O DECISIÓN
if (edad >= 18 and edad <= 110): # Rango de 18 a 110
  print("Mayor de edad")
elif (edad >= 0 and edad < 18): # Rango de 0 hasta menor que 18
  print("Menor de edad")
elif (edad < 0 or edad > 110): # Edades Inválidas menor que 0 y mayor que 120
  print("Edad Inválida")


'''
EJERCICIO 1. CONDICIONES
APROBADO              Entre 6 y 10
APROBADO DE PANSASO   Equivalente a 6
REPROBADO             Entre 0 y menor que 6
PROMEDIO INVÁIDO      Menor que 0 o mayor que 10
'''
