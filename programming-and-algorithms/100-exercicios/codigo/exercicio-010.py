salario_fixo = float(input("Salário fixo: "))
total_vendido = float(input("Total vendido: "))
comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao
print(f"Comissão: {comissao:.2f}")
print(f"Salário total: {salario_total:.2f}")
