class Produto:
    def __init__(self, id, nome, preco, tamanho):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "tamanho": self.tamanho
        }
    
    def __repr__(self):
        return f"Produto(id={self.id}, nome={self.nome}, preco={self.preco}, tamanho={self.tamanho})"