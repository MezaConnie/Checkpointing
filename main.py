# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:25:29 2022

@author: macon
"""

from alumnos import Alumnos
from alumno import Alumno
from os import system
import pickle
import os


def cadenaVacia(cadena):
    if len(cadena) == 0:
        return True
    return False

def clear():
    input()
    system('cls')


def menu(a:Alumnos):
    while True:
        print("\t\t\t   --Club de Algoritmia--")
        print("1. Agregar Alumno \t\t\t\t\t2. Alumnos Registrados")
        print("3. Buscar Alumno por codigo \t\t0. Salir")
        op = input("Opcion: ")

        if (op == "2" or op == "3") and a.vacia():
            print("No hay Alumnos Registrados aun.\n")
            continue

        if op == "1":
            print("\nAGREGAR ALUMNO")
            bandera = False
            while not bandera:
                try:
                    codigo = int(input("Código de Alumno: "))                 
                    nombre = input("Nombre (comenzando por apellidos): ")
                    carrera = input("Carrera: ")
                    if cadenaVacia(nombre) or cadenaVacia(carrera):
                        raise Exception("Cadena vacia no permitida.")
                    semestre = int(input("Semestre: "))
                    
                    alumno = Alumno(codigo, nombre, carrera, semestre)

                    if a.agregar(alumno):
                        print("\nRegistrado.")
                        bandera = True
                        menu(a)
                    else:
                        clear()
                except:
                    print("\n**Datos invalidos.**\nAsegúrese de ingresar:\nCódigo entero de 9 digitos.")
                    print("Nombre y Carrera como cadenas.\nSemestre entero no menor a 1 ni mayor a 16.")
                
        elif op == "2":
            print("\n\t  Alumnos Registrados")
            a.mostrar()
            
        elif op == "3":
            a.buscar()

        elif op == "0":
            print("Vuelva pronto")
            break
        
        else:
            print("Opcion no valida.")    
        
        fileHandler = open("alumnos", "wb")
        
        pickle.dump(a, fileHandler)
            
        fileHandler.close()
        
        clear()

a = Alumnos()

if os.path.exists("alumnos"):
    tam_archivo = os.stat("alumnos").st_size 
    if tam_archivo != 0:
        try:
                pickle_in = open("alumnos", "rb")
                alumnos = pickle.load(pickle_in)
                pickle_in.close()
                menu(alumnos)
        except:
                raise Exception("Error al restaurar.")
        finally:
                pickle_in.close() 
    else:
        menu(a)

menu(a)