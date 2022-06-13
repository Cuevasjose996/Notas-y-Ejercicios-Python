"""Crear un programa que tenga dos funciones, 
una que contenga el area de un cuadrado con argumentos de base y altura; 
y la otra el area de un circulo con argumento de radio"""
from cmath import pi
import math 

def areacuadrado(base,altura):
    return base*altura

def areacirculo(radio):
    area=pi*pow(radio,2)
    return area

print(areacuadrado(50,20))
print(areacirculo(10))