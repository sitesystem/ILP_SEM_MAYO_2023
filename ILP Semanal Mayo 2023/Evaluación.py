import os
clear = lambda: os.system('cls')

aciertos = 0
opcion = 0
respuesta = "si"

def Menú():
  print("--- MENÚ DE OPCIONES ---")
  print("1. Cuestionario")
  print("2. Mostrar Resultados")
  print("3. Salir")

def Cuestionario():
  print("Cargando Cuestionario ...")

def MostrarResultados():
  print("Total de aciertos: ", aciertos)
  print("Calificación Final: ", (aciertos * 10) / 12)

while (respuesta == "si" or respuesta == "Si" or respuesta == "s"):
  Menú() # Mando a llamar o invoco la función
  opcion = int(input("Elige una opción: "))
  if (opcion == 1):
    Cuestionario()
  elif (opcion == 2):
    MostrarResultados()
  else:
    break
  respuesta = input("¿Quieres continuar? (s/n): ")
  clear()
