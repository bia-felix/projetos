class ContaBancaria: 
    def __init__ (self, saldo):
        self.__saldo= saldo
      
    def depositar (self):
        acrescentar = int(input("Digite um valor para depositar:"))
        self.__saldo += acrescentar
        print (f"{self.__saldo} reais")
        
    def sacar (self):
        decrementar = int(input("Digite um valor para sacar: "))
        
        if (decrementar <= self.__saldo):
            self.__saldo -= decrementar 
            print ("saldo atualiazado:", self.__saldo)
            
        else:
            print("saldo insuficiente: R$", self.__saldo)
        
conta = ContaBancaria(0)

conta.depositar()
conta.sacar()
           
