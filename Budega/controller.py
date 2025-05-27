from User import User
from time import sleep
from Produto import Produto
from controller_estoque import Estoque

usuarios = []

estoque = Estoque(Produto(0, "", 0.0, ""))  
estoque.iniciar_arquivo()

def registrar():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    for u in usuarios:
        if u.nome == nome:
            print("⚠️ Usuário já existe!")
            return

    novo_usuario = User(nome, senha)
    usuarios.append(novo_usuario)
    print("✅ Usuário registrado com sucesso!")

def login():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    for u in usuarios:
        if u.nome == nome and u.senha == senha:
            print(f"✅ Bem-vindo, {u.nome}!")
            return True
    print("❌ Usuário ou senha incorretos.")
    return False

def menu_estoque():
    while True:
        print("\n=== MENU ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Deletar produto")
        print("3 - Listar produto")
        print("4 - Editar produto")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id_produto = int(input("ID: "))
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                tamanho = input("Tamanho: ")
                estoque.cadastrar_produto(id_produto, nome, preco, tamanho)
            except ValueError:
                print("❌ Dados inválidos.")

        elif opcao == "2":
            try:
                id_produto = int(input("ID do produto a deletar: "))
                estoque.deletar_produto(id_produto)
            except ValueError:
                print("❌ ID inválido.")

        elif opcao == "3":
            estoque.listar_produto()

        elif opcao == "4":
            try:
                id_produto = int(input("ID do produto a editar: "))
                nome = input("Novo nome (deixe vazio para não alterar): ")
                preco = input("Novo preço (deixe vazio para não alterar): ")
                tamanho = input("Novo tamanho (deixe vazio para não alterar): ")

                novo_nome = nome if nome else None
                novo_preco = float(preco) if preco else None
                novo_tamanho = tamanho if tamanho else None

                estoque.atualizar_produto(id_produto, novo_nome, novo_preco, novo_tamanho)
            except ValueError:
                print("❌ Dados inválidos.")
                
        elif opcao == "5":
            print("Encerrando submenu de estoque...")
            sleep(2)
            break

        else:
            print("❌ Opção inválida!")

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Registrar")
        print("2 - Login")
        print("3 - Estoque")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar()
        elif opcao == "2":
            if login():
                menu_estoque()
        elif opcao == "3":
            print("⚠️ Faça login antes de acessar o estoque.")
        elif opcao == "4":
            print("Encerrando o sistema...")
            sleep(2)
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()
