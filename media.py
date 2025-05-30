nome=input("digite o nome do aluno:")
nota1=float(input("digite a primeira nota:"))
nota2=float(input("digite a segunda nota:"))
media=(nota1+nota2)/2
print("nome do aluno:",nome)
print("primeira nota é:",nota1)
print("segunda nota é:",nota2)
print("a media é:",media)
if media >7:
    print("aluno foi aprovado")
else:
    print("O aluno foi reprovado")
