from Produto import Produto
import json
import os
from pathlib import Path

class Estoque:
    def __init__(self, produto: Produto):
        self.produto = produto
        self.CAMINHO_ARQUIVO = Path(__file__).parent / "produtos.json"

    def iniciar_arquivo(self):
        if not self.CAMINHO_ARQUIVO.exists():
            self.salvar_produtos([])
            print(f"Arquivo {self.CAMINHO_ARQUIVO} criado com lista de produtos vazia")

    def salvar_produtos(self, produtos: list):
        try:
            with open(self.CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {e}")

    def carregar_produtos(self) -> list:
        if not self.CAMINHO_ARQUIVO.exists():
            return []

        try:
            with open(self.CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                if not conteudo:
                    return []

                produtos = json.loads(conteudo)

                if not isinstance(produtos, list):
                    print(f"Alerta: O arquivo {self.CAMINHO_ARQUIVO} não tem uma lista válida. Criando nova.")
                    return []

                return produtos
        except json.JSONDecodeError:
            print("Erro ao decodificar arquivo JSON")
            return []

        except IOError as e:
            print("Erro ao ler o arquivo")
            return []

    def cadastrar_produto(self, id_produto: int, nome: str, preco: float, tamanho: str):
        produtos = self.carregar_produtos()

        for prod in produtos:
            if prod.get("id") == id_produto:
                print("Produto com esse ID já existe!")
                return

        novo_produto = Produto(id_produto, nome, preco, tamanho)
        produto_dict = novo_produto.to_dict()

        produtos.append(produto_dict)
        self.salvar_produtos(produtos)
        print(f"Produto {nome} cadastrado com sucesso")

    def listar_produto(self):
        produtos = self.carregar_produtos()

        if not produtos:
            print("Nenhum produto cadastrado")
            return

        print("\n=== Lista de Produtos ===")
        for prod in produtos:
            print(f"ID: {prod.get('id')}, Nome: {prod.get('nome')}, Preço: {prod.get('preco')}, Tamanho: {prod.get('tamanho')}")

    def atualizar_produto(self, id_alvo: int, novo_nome: str = None, novo_preco: float = None, novo_tamanho: str = None):
        produtos = self.carregar_produtos()
        produto_encontrado = False

        for prod in produtos:
            if prod.get("id") == id_alvo:
                produto_encontrado = True
                if novo_nome:
                    prod["nome"] = novo_nome
                if novo_preco is not None:
                    prod["preco"] = novo_preco
                if novo_tamanho:
                    prod["tamanho"] = novo_tamanho

                self.salvar_produtos(produtos)
                print("Produto atualizado com sucesso")
                return

        if not produto_encontrado:
            print("Produto não encontrado")

    def deletar_produto(self, id_produto: int):
        produtos = self.carregar_produtos()
        produtos_filtrados = [p for p in produtos if p["id"] != id_produto]

        if len(produtos) == len(produtos_filtrados):
            print("Produto não encontrado")
        else:
            self.salvar_produtos(produtos_filtrados)
            print("Produto deletado com sucesso")
