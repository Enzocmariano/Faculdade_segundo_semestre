import math

def encontrar_maior(a, b, c):
    if a >= b and a >= c:
     return a
    if b >= c and b >= a:
     return b
    if c >= b and c >= a:
     return c

a1 = float(input("De valor para A: "))
b1 = float(input("De valor para b: "))
c1 = float(input("De valor para c: "))

maior = encontrar_maior(a1, b1, c1)

print(f"Maior numero é {maior}")