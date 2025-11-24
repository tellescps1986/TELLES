class Trabalhador:
    #1° Membro da Classe - Atributos
    __nome: str
    __jornada: float

    #2° Membro da Classe - Propriedade
    @property
    def _nome(self) -> str:
        return self.__nome
    
    @_nome.setter
    def _nome(self, nome: str):
        if nome == "" or nome is None:
            raise ValueError("Nome Inválido")
        self.__nome = nome

    @property
    def _jornada(self) -> float:
        return self.__jornada
    
    @_jornada.setter
    def _jornada(self, jornada: float):
        if jornada <= 0:
            raise ValueError("Jornada Inválida")
        self.__jornada = jornada

    #3° Membro da Classe - Construtor
    def __init__(self, nome: str, jornada: float):
        self._nome = nome
        self._jornada = jornada

    #4° Membro da Classe - Métodos
    def pagamento(self) -> float:
        return 0


class EmpregadoSenai(Trabalhador):
    __valorPorHora: float

    @property
    def _valorPorHora(self) -> float:
        return self.__valorPorHora
    
    @_valorPorHora.setter
    def _valorPorHora(self, valor: float):
        if valor <= 0:
            raise ValueError("Valor por hora inválido")
        self.__valorPorHora = valor

    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada)
        self._valorPorHora = valor

    def pagamento(self):
        return self._jornada * self._valorPorHora


class Terceirizado(EmpregadoSenai):
    __adicional = 0.2

    def __init__(self, nome, jornada, valor):
        super().__init__(nome, jornada, valor)

    def pagamento(self):
        return super().pagamento() * (1 + self.__adicional)


lista = []


def main():
    quantidade = int(input("Digite a quantidade de funcionários: "))

    for i in range(quantidade):
        print(f"\nColaborador n° {i + 1}")
        
        colaborador = input("O colaborador é terceirizado (s/n)? ").strip().lower()
        nome = input("Nome do Colaborador: ")
        horas = float(input("Horas Trabalhadas: "))
        valor = float(input("Valor da Hora Trabalhada: "))

        if colaborador == "s":
            funcionario = Terceirizado(nome, horas, valor)
        else:
            funcionario = EmpregadoSenai(nome, horas, valor)

        lista.append(funcionario)

    print("\n--- Pagamentos dos Colaboradores ---")
    for colaborador in lista:
        print(f"{colaborador._nome} - R$ {colaborador.pagamento():.2f}")


if __name__ == "__main__":
    main()
