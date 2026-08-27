nome = input ("Qual seu nome? ")
print("É um prazer te conhecer", nome)
print("Me chamo Ozne2.3")
print("Estou aqui pra te contar uma historia")
while True:
  Questão = input ("Você gostaria de ouvir essa histoia? ")
  if Questão.lower() == "sim":
    print("Tudo bem, então  vamos lá")
    print("Marcos era um programador júnior em uma pequena startup de tecnologia.")
    print("Todas as noites, ele ficava até tarde tentando resolver um bug complicado.")
    print("O sistema que ele mantinha processava dados críticos para milhares de usuários.")
    print("Numa sexta-feira, um erro misterioso derrubou o servidor de produção.")
    print("O time inteiro entrou em pânico, mas Marcos respirou fundo e começou a investigar.")
    print("Ele abriu os logs e percebeu que o problema vinha de uma função antiga, mal documentada.")
    print("Sem perder a calma, ele isolou o trecho de código suspeito e criou um ambiente de teste.")
    print("Hora após hora, ele testava hipóteses, uma por uma, eliminando possibilidades.")
    print("Por volta da meia-noite, encontrou a causa: um loop que nunca era encerrado corretamente.")
    print("Corrigiu o erro, escreveu testes automatizados e documentou tudo com cuidado.")
    print("Ao subir a correção, o servidor voltou a funcionar perfeitamente.")
    print("Na segunda-feira, o time todo reconheceu o esforço de Marcos.")
    print("Ele aprendeu que resolver problemas difíceis exige paciência, não apenas pressa.")
    print("Também entendeu a importância de documentar bem o código para o futuro.")
    print("Com o tempo, Marcos se tornou referência em debugging na empresa.")
    print("E cada novo desafio só fortalecia sua paixão por programar.") 
    print("Essa foi a hitoria para te fazer pensar um pouco, Muito obrigado pela atenção")
    break
  elif Questão.lower() == "não":
    print("Tudo bem meu jovem")
    print("Deixaremos essa historia para outro dia")
    break
  else:
    print("Perdão não entendi, responda com sim ou não")
