# This is a sample Python script.
# Sistema simples de controle de estoque
# Atividade prática - Engenharia de Software

# Dicionário com os produtos cadastrados e suas quantidades no estoque
estoque = {
    "caneta": 50,
    "caderno": 30,
    "lapis": 40
}

# Lista usada para guardar o histórico de entradas e saídas
movimentacoes = []


# Função para mostrar todos os produtos cadastrados
def mostrar_estoque():
    print("\n--- ESTOQUE ATUAL ---")

    for produto in estoque:
        print(produto, "-", estoque[produto], "unidades")


# Função para registrar entrada de produto
def entrada_produto():
    print("\n--- ENTRADA DE PRODUTO ---")

    mostrar_estoque()

    produto = input("Digite o nome do produto: ").lower()

    # Verifica se o produto existe no estoque
    if produto in estoque:
        quantidade = int(input("Digite a quantidade recebida: "))
        data = input("Digite a data da entrada: ")

        # Atualiza o estoque somando a quantidade recebida
        estoque[produto] = estoque[produto] + quantidade

        # Guarda a movimentação realizada
        movimentacoes.append("Entrada de " + str(quantidade) + " unidade(s) de " + produto + " em " + data)

        print("Entrada registrada com sucesso!")
    else:
        print("Produto não cadastrado.")


# Função para registrar saída de produto
def saida_produto():
    print("\n--- SAÍDA DE PRODUTO ---")

    mostrar_estoque()

    produto = input("Digite o nome do produto: ").lower()

    # Verifica se o produto existe no estoque
    if produto in estoque:
        quantidade = int(input("Digite a quantidade retirada: "))

        # Verifica se existe quantidade suficiente no estoque
        if quantidade <= estoque[produto]:
            data = input("Digite a data da saída: ")
            responsavel = input("Digite o nome do responsável: ")

            # Atualiza o estoque diminuindo a quantidade retirada
            estoque[produto] = estoque[produto] - quantidade

            # Guarda a movimentação realizada
            movimentacoes.append("Saída de " + str(quantidade) + " unidade(s) de " + produto + " em " + data + " - Responsável: " + responsavel)

            print("Saída registrada com sucesso!")
        else:
            print("Quantidade insuficiente no estoque.")
    else:
        print("Produto não cadastrado.")


# Função para mostrar o histórico de movimentações
def mostrar_movimentacoes():
    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")

    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
    else:
        for item in movimentacoes:
            print(item)


# Menu principal do sistema
while True:
    print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
    print("1 - Mostrar estoque")
    print("2 - Registrar entrada de produto")
    print("3 - Registrar saída de produto")
    print("4 - Mostrar movimentações")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        entrada_produto()
    elif opcao == "3":
        saida_produto()
    elif opcao == "4":
        mostrar_movimentacoes()
    elif opcao == "5":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")