# ==========================================
# 1. IMPORTS DE MÓDULOS
# ==========================================


import math

def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(cateto_a ** 2 + cateto_b ** 2)

A = float(input("Cateto a: "))
B = float(input("Cateto b: "))

calcular_hipotenusa(A,B)

print(f"{calcular_hipotenusa}")