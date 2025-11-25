class Contribuinte:
    __nome: str
    __rendaAnual: float

    @property
    def _nome(self) -> str:
        return self.__nome
    
    @_nome.setter
    def _nome(self, nome:str):
        if nome == "" or nome is None:
            raise ValueError("Nome Inválido")
        self.__nome = nome

    @property
    def _rendaAnual(self) -> str:
        return self.__rendaAnual
    
    @_rendaAnual.setter
    def _rendaAnual(self, rendaAnual: float):
        if rendaAnual <= 0:
            raise ValueError("Renda Inválida")
        self.__rendaAnual = rendaAnual


    def __init__(self, nome:str, jornada:float):
        self._nome = nome
        self._rendaAnual = rendaAnual
    
    def calculo(self) -> float:
        if self._rendaAnual < 20000:
            return (self._rendaAnual - (self.__rendaAnual*0.15))
        else:
            return (self._rendaAnual - (self.__rendaAnual*0.25))



class PessoaFisica(Contribuinte):
    __gastoComSaude: float

    @property
    def _gastoComSaude(self) -> float:
        return self.__gastoComSaude
    
    @_gastoComSaude.setter
    def _gastoComSaude(self, gastoComSaude:float):
        if gastoComSaude <=0:
            raise ValueError("Valor inválido")
        self.__gastoComSaude = gastoComSaude

    def __init__(self, nome, rendaAnual, gastoComSaude):
        super().__init__(nome, rendaAnual)
        self._gastoComSaude = gastoComSaude

    def calculo(self):
        if self._numeroFuncionarios > 10:
            return (self._numeroFuncionarios - (self.__rendaAnual*0.14))
        else:
            return (self._numeroFuncionarios - (self.__rendaAnual*0.16))


class PessoaJuridica(Contribuinte):
    __numeroFuncionarios: float

    @property
    def _numeroFuncionarios(self) -> float:
        return self.__numeroFuncionarios
    
    @_numeroFuncionarios.setter
    def _numeroFuncionarios(self, numeroFuncionarios:float):
        if numeroFuncionarios <=0:
            raise ValueError("Valor inválido")
        self.__numeroFuncionarios = numeroFuncionarios

    def __init__(self, nome, rendaAnual, numeroFuncionarios):
        super().__init__(nome, rendaAnual)
        self._numeroFuncionarios = numeroFuncionarios

    def calculo(self):
        pass

lista=[]


def main():
    N = int(input("Digite a quantidade de funcionários: "))
    pessoa = str(input("Digite F para Pessoa Física e J para Pessoa Jurídica: "))

    for i in range(N):
        if(pessoa == "F"):
            nome = input("Digite o nome do Colaborador: ")
            rendaAnual = float(input("Digite a Renda Anual do Colaborador: "))
            gastoComSaude = float(input("Digite o Gasto Anual com Saúde: "))

            contribuinte = PessoaFisica(nome, rendaAnual, gastoComSaude)

        elif(pessoa == "J"):
            nome = input("Digite o nome do Colaborador: ")
            rendaAnual = float(input("Digite a Renda Anual do Colaborador: "))
            NumeroFuncionarios = int(input("Digite o Número de Funcionários: "))

            contribuinte = PessoaJuridica(nome, rendaAnual, NumeroFuncionarios)

        else:
            print("Digite pessoa Física ou Jurídica")
                  
        lista.append(contribuinte)
    for pessoa in lista:
        print(f"{pessoa._nome} - Renda Anual R$ {pessoa._rendaAnual}- Gasto Anual com Saúde R$ {pessoa._gastoAnual}")

if __name__ == "__main__":
    main()