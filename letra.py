palavra=input("Digite uma palavra ou frase:")
vogal=['a','e','i','o','u']
casa=['b','c','d']
contador=0

for letra in palavra:
    if letra in vogal:
        contador+=1
print(contador)
    
