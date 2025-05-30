num1=float(input("digite um numero:"))
num2=float(input("digite outo numero:"))
operacao=input("digite a operação:")

if operacao == "adicao":
    resultado=num1+num2
    
elif operacao=="subtracao":
    
    resultado=num1-num2

elif operacao=="multiplicacao":
    
     resultado=num1*num2
   
elif operacao=="divisao":
     
    resultado=num1/num2
   
else:
    print("Digite algo válido")
print("resoltado é:",resultado)
