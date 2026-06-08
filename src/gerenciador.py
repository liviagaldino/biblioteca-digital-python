import os

PASTA_DOCUMENTOS = "../documentos"


def listar_documentos():

    print("\n=== DOCUMENTOS ENCONTRADOS ===")

    encontrou = False

    for raiz, diretorios, arquivos in os.walk(PASTA_DOCUMENTOS):

        for arquivo in arquivos:

            encontrou = True
            print(f"- {arquivo}")

    if not encontrou:
        print("Nenhum documento encontrado.")


def adicionar_documento():

    nome = input("Nome do documento: ")
    ano = input("Ano de publicação: ")

    extensao = nome.split(".")[-1].upper()

    pasta_destino = os.path.join(
        PASTA_DOCUMENTOS,
        extensao,
        ano
    )

    os.makedirs(pasta_destino, exist_ok=True)

    caminho = os.path.join(pasta_destino, nome)

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("Documento criado pelo sistema.")

    print("Documento adicionado com sucesso.")


def renomear_documento():

    antigo = input("Nome atual: ")
    novo = input("Novo nome: ")

    caminho_antigo = os.path.join(PASTA_DOCUMENTOS, antigo)
    caminho_novo = os.path.join(PASTA_DOCUMENTOS, novo)

    if os.path.exists(caminho_antigo):

        os.rename(caminho_antigo, caminho_novo)
        print("Documento renomeado.")

    else:

        print("Documento não encontrado.")


def remover_documento():

    nome = input("Nome do documento: ")

    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if os.path.exists(caminho):

        os.remove(caminho)
        print("Documento removido.")

    else:

        print("Documento não encontrado.")