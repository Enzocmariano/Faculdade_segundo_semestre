"""
Exercício 31 - Divisível por 3 e por 5
Módulo 02: Estruturas Condicionais
"""
numero = int(input("Digite um número
inteiro: "))
div3 = numero % 3 == 0
div5 = numero % 5 == 0
if div3 and div5:
    print("DIVISÍVEL POR 3 E 5")
elif div3:
    print("DIVISÍVEL APENAS POR 3")
elif div5:
    print("DIVISÍVEL APENAS POR 5")
else:
    print("NÃO DIVISÍVEL POR 3 NEM 5")
