import math 

numero = float(input("Digite um valor decimal inteiro: "))

print(f"Raiz quadrada: {math.sqrt(numero)}")
print(f"Arredondado para cima: {math.ceil(numero)}")
print(f"Arredondado para Baixo: {math.floor(numero)}")

Raio = input("Digite um valor para o raio: ")
calcular_area_circulo = Raio * 2

print(f"{math.pi(calcular_area_circulo)}")