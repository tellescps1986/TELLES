class Contribuinte:
    __nome: str
    __rendaAnual: float

    @property
    def _nome(self) -> str:
        return self.__nome
    
    @_nome.setter
    def _nome(self, nome: str):
        if not nome:
            raise ValueError("Nome Inválido")
        self.__nome = nome

    @property
    def _rendaAnual(self) -> float:
        return self.__rendaAnual
    
    @_rendaAnual.setter
    def _rendaAnual(self, rendaAnual: float):
        if rendaAnual <= 0:
            raise ValueError("Renda Inválida")
        self.__rendaAnual = rendaAnual

    def __init__(self, nome: str, rendaAnual: float):
        self._nome = nome
        self._rendaAnual = rendaAnual
    
    def calculo(self) -> float:
        if self._rendaAnual < 20000:
            return self._rendaAnual * 0.15
        else:
            return self._rendaAnual * 0.25


class PessoaFisica(Contribuinte):
    __gastoComSaude: float

    @property
    def _gastoComSaude(self) -> float:
        return self.__gastoComSaude
    
    @_gastoComSaude.setter
    def _gastoComSaude(self, gastoComSaude: float):
        if gastoComSaude < 0:
            raise ValueError("Valor inválido")
        self.__gastoComSaude = gastoComSaude

    def __init__(self, nome, rendaAnual, gastoComSaude):
        super().__init__(nome, rendaAnual)
        self._gastoComSaude = gastoComSaude

    def calculo(self):
        imposto_base = super().calculo()
        desconto_saude = self._gastoComSaude * 0.5
        return max(imposto_base - desconto_saude, 0)


class PessoaJuridica(Contribuinte):
    __numeroFuncionarios: int

    @property
    def _numeroFuncionarios(self) -> int:
        return self.__numeroFuncionarios
    
    @_numeroFuncionarios.setter
    def _numeroFuncionarios(self, numeroFuncionarios: int):
        if numeroFuncionarios <= 0:
            raise ValueError("Valor inválido")
        self.__numeroFuncionarios = numeroFuncionarios

    def __init__(self, nome, rendaAnual, numeroFuncionarios):
        super().__init__(nome, rendaAnual)
        self._numeroFuncionarios = numeroFuncionarios

    def calculo(self):
        if self._numeroFuncionarios > 10:
            return self._rendaAnual * 0.14
        else:
            return self._rendaAnual * 0.16


lista = []


def main():
    N = int(input("Digite a quantidade de contribuintes: "))

    for i in range(N):
        pessoa = input("Digite F para Pessoa Física e J para Pessoa Jurídica: ").upper()

        if pessoa == "F":
            nome = input("Nome: ")
            renda = float(input("Renda anual: "))
            gasto = float(input("Gasto anual com saúde: "))
            contribuinte = PessoaFisica(nome, renda, gasto)

        elif pessoa == "J":
            nome = input("Nome: ")
            renda = float(input("Renda anual: "))
            num = int(input("Número de funcionários: "))
            contribuinte = PessoaJuridica(nome, renda, num)

        else:
            print("Tipo inválido!")
            continue

        lista.append(contribuinte)

    print("\n===== RESULTADOS =====")
    for pessoa in lista:
        imposto = pessoa.calculo()
        print(f"{pessoa._nome} — Imposto devido: R$ {imposto:.2f}")


if __name__ == "__main__":
    main()
