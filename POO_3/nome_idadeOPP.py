 # Atributos
class Nome_Idade:
    nome:str  
    idade:int
        
    #Construtor
    def __init__(self, nome:str="", idade:int=0):
        self.nome = nome      
        self.idade = idade

     # Métodos
    def pessoaMaisVelha(self, outra_idade) -> bool:
       return self.idade > outra_idade

class Nome_Salario:
    nome:str  
    salario:float

    def __init__(self, nome:str="", salario:float=0):
        self.nome = nome     
        self.salario = salario
    
    def mediaSalario(self, outro_salario) -> float:
       return (self.salario + outro_salario)/2
    


