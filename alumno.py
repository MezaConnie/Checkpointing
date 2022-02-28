# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:26:18 2022

@author: macon
"""

class Alumno:
    def __init__(self, codigo:int, nombre:str, carrera:str, semestre:int):
        self.__codigo = codigo 
        self.__nombre = nombre 
        self.__carrera = carrera 
        self.__semestre = semestre
    
    def __str__(self):
        return f"Codigo de Alumno: {self.__codigo}\nNombre: {self.__nombre}\ncarrera: {self.__carrera}\nSemestre: {self.__semestre}\n\n"
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def carrera(self):
        return self.__carrera

    @property
    def semestre(self):
        return self.__semestre

    def imprimir(self):
        print("--------------------------------")
        print("Codigo de Alumno: ", self.__codigo)
        print("Nombre: ", self.__nombre.upper())
        print("Carrera: ", self.__carrera.upper())
        print("Semestre: ", self.__semestre)