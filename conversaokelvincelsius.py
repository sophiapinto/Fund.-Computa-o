# Conversão de Celsius/Kelvin  
# Código by: Sarah Sophia Pinto
# Universidade Federal do Maranhão-UFMA
# Curso: BICT   2°período     Turma: 23456M123

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:55:53 2020

@author: Sarah Sophia Pinto
"""

# Conversor de Unidades: Graus Celsius e Fahrenheit

def menu_inicial ():
    print("Conversão de Temperaturas")
    print("1. Converter de Celsius para Kelvin")
    print("2. Converter de Kelvin para Celsius")

def cel_kelvin():
    
    C = float (input ("Digite a temperatura em graus Celsius:   "))
    K = C + 273
    print("O valor da temperatura em Kelvin é:  ", K, "K.")

def kelvin_cel():
    K = float (input("Digite a temperatura em Kelvin:   "))
    C = K - 273
    print("O valor da temperatura em Celsius é:  ", C, "°C.")

if __name__=='__main__':
    menu_inicial()
    escolha = input("Qual o tipo de conversão que deseja realizar?")

    if escolha == '1':
        cel_kelvin()

    if escolha == '2':
        kelvin_cel()