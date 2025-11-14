class Produto:
    #Atributos
    nome: str
    preco: float
    saldo: int

    #Métodos
    def valorTotalEmEstoque(self) -> float:
        return self.preco * self.saldo
    
    def adicionarProdutos(self, quantidade) -> int:
       self.saldo += quantidade
       return self.preco
    
    def removerProdutos(self, quantidade) -> int:
        self.saldo -= quantidade
        return self.preco
