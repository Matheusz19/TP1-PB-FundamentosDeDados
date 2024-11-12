tarefas = []

def adicionar_tarefa(tarefa: str):
    """
    Adiciona uma nova tarefa à lista de tarefas pendentes.

    Parâmetros:
        tarefa (str): A descrição da tarefa a ser adicionada.

    Retorno:
        None
    """
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    """
    Lista todas as tarefas pendentes, enumerando-as.

    Retorno:
        None
    """
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['tarefa']} - Status: {status}")

def marcar_concluida(indice: int):
    """
    Marca uma tarefa específica como concluída.

    Parâmetros:
        indice (int): O índice da tarefa a ser marcada como concluída.

    Retorno:
        None
    """
    if 0 <= indice < len(tarefas):
        if not tarefas[indice]["concluida"]:
            tarefas[indice]["concluida"] = True
            print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída!")
        else:
            print("Essa tarefa já está concluída.")
    else:
        print("Índice inválido. Tente novamente.")

def remover_tarefa(indice: int):
    """
    Remove uma tarefa da lista de tarefas.

    Parâmetros:
        indice (int): O índice da tarefa a ser removida.

    Retorno:
        None
    """
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")

def menu():
    """
    Exibe o menu de opções e processa a escolha do usuário.

    Retorno:
        None
    """
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número entre 1 e 5.")
            continue

        if opcao == 1:
            tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 3:
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a marcar como concluída: ")) - 1
                marcar_concluida(indice)
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == 4:
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a remover: ")) - 1
                remover_tarefa(indice)
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        elif opcao == 5:
            print("Saindo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()