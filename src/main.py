from gerenciador import (
    listar_documentos,
    adicionar_documento,
    renomear_documento,
    remover_documento
)

while True:

    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1 - Listar documentos")
    print("2 - Adicionar documento")
    print("3 - Renomear documento")
    print("4 - Remover documento")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_documentos()

    elif opcao == "2":
        adicionar_documento()

    elif opcao == "3":
        renomear_documento()

    elif opcao == "4":
        remover_documento()

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")