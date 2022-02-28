# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:26:18 2022

@author: macon
"""

from alumno import Alumno
from os import system

def clear():
    input()
    system('cls')

class Alumnos:
    def __init__(self):
        self.__lista = []
    
    def listaHecha(self, lista:list):
        self.__lista = lista

    def agregar(self, alumno:Alumno):
        try:
            if len(str(alumno.codigo)) != 9 or alumno.semestre < 1 or alumno.semestre > 16: 
                raise ValueError("Dato invalido.") 
            if not self.duplicado(alumno):
                self.__lista.append(alumno)
                return True
        except ValueError as v:
            print(v) 
            return False
    
    def buscar(self):
        try:
            i = 0  
            while i != 3:
                codigo = int(input("Codigo de alumno: "))
                for a in self.__lista:
                    if codigo == a.codigo:
                        a.imprimir()
                        return
                i += 1
                print("Registro no encontrado.")
                clear()
                
            if i == 3:
                raise Exception("Límite de intentos excedido.")       
        except Exception as v:
            print(v)
            
        
    def mostrar(self):
        for a in self.__lista:
            a.imprimir()
    
    def vacia(self):
        if len(self.__lista) == 0:
            return True
        else:
            return False

   
    def duplicado(self, a:Alumno):
        try:
            for alumno in self.__lista:
                if a.codigo == alumno.codigo:
                    raise ValueError("Codigo ya registrado.")
            return False
        except ValueError as v:
            print(v)
            return True