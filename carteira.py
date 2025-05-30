nome=input("digite o seu nome:")
idade =float(input("Digite a sua idade: "))
carteira=input("vc possui carteira de motorista:")
if idade > 18 and carteira=="sim":
    print(nome,"apto a dirigir e ter a carteira")
else:
    print(nome,"nn esta apto a dirigir e  ter a carteira")
