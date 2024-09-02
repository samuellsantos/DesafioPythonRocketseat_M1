def adicionarContato(contatos, nome, telefone, email, favorito):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(contato)

    print(f"O contato {nome} foi adicionado com sucesso!")
    return

def visualizarContatos(contatos):
    print("\n Lista de contatos")

    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = contato["favorito"]
        stsFavorito = "✔" if favorito else "✘"


        print(f"[{indice}]. nome: {nome} - Telefone: {telefone} - email: {email} - favorito: {stsFavorito}")

def editarContato(contatos, indice, novoNome, novoTelefone, novoEmail):
    indice_ajustado = indice - 1
    nome_antes = contatos[indice_ajustado]["nome"]
    telefone_antes = contatos[indice_ajustado]["telefone"]
    email_antes = contatos[indice_ajustado]["email"]
    

    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        if novoNome == '':
            contatos[indice_ajustado]["nome"] = nome_antes
        else:
            contatos[indice_ajustado]["nome"] = novoNome

        if novoTelefone == '':
            contatos[indice_ajustado]["telefone"] = telefone_antes
        else:
            contatos[indice_ajustado]["telefone"] = novoTelefone

        if novoEmail == '':
            contatos[indice_ajustado]["email"] = email_antes
        else:
            contatos[indice_ajustado]["email"] = novoEmail

        print(f"O contato com o índice {indice} foi modificado com sucesso!")
    else:
        print("O indice não é valido.")
    return
        
def ToggleFav(contatos, indice):
    indice_ajustado = indice - 1
    contato = contatos[indice_ajustado]["nome"]
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        if contatos[indice_ajustado]["favorito"] == True:
            contatos[indice_ajustado]["favorito"] = False
            print(f"O contato {contato} foi modifado para não favorito.")
        else:
            contatos[indice_ajustado]["favorito"] = True
            print(f"\nO contato {contato} foi modifado para favorito.")
    else:
        print("Indice inválido.")

    return

def exibirFavoritos(contatos):
        print("\n Lista de contatos favoritos")
        for indice, contato in enumerate(contatos, start=1):
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            favorito = contato["favorito"]
            stsFavorito = "✔" if favorito else "✘"
            if favorito:
                print(f"[{indice}]. nome: {nome} - Telefone: {telefone} - email: {email} - favorito: {stsFavorito}")

def deletarContato(contatos, indice):
    indice_ajustado = indice - 1
    del contatos[indice_ajustado]
    print(f"Contato com o indice {indice} foi deletado.")



       





contatos = []
while True:
    print("\n______Agenda de contatos______")
    print("[1] Adicionar um novo contato.")
    print("[2] Visualizar lista de contatos.")
    print("[3] Editar contato.")
    print("[4] Marcar/desmarcar contato como favorito.")
    print("[5] Exibir contatos favoritos.")
    print("[6] Deletar contato.")

    escolha = int(input("\nDigite sua escolha: "))

    if escolha == 1:
        print("\n Adicionar novo Contato")
        nome = input("Digite o nome: ")
        telefone = input("Digite o número de telefone: ")
        email = input("Digite o E-mail: ")
        favorito = input("\nFavoritar ? [S] Sim - [N] Não:  ")
        favorito = favorito.upper()

        while favorito != "S" and favorito != "N":
            print(f"O valor digitado não é válido.")
            favorito = input("\nFavoritar ? [S] Sim - [N] Não:  ")
            favorito = favorito.upper()
        if favorito == "S":
            favorito = True
        else:
            favorito = False

        adicionarContato(contatos, nome, telefone, email, favorito)
    if escolha == 2:
        if len(contatos) == 0:
            print("A lista de contatos está vazia.")
        else:
            visualizarContatos(contatos)
    if escolha == 3:
        visualizarContatos(contatos)
        indice = int(input("Digite o Índice do contato: "))
        print("\nSe quiser manter os dados anteriores deixe o campo vazio.")
        nome = input("Digite um novo nome: ")
        telefone = input("Digite um novo telefone: ")
        email = input("Digite um novo E-mail: ")
        editarContato(contatos, indice, nome, telefone, email)
    if escolha == 4:
        visualizarContatos(contatos)
        indice = int(input("\nDigite o indice para favoritar/desfavoritar: "))
        ToggleFav(contatos, indice)
    if escolha == 5:
        exibirFavoritos(contatos)
    if escolha == 6:
        visualizarContatos(contatos)
        indice = int(input("Digite o indice do contato que deseja deletar: "))
        deletarContato(contatos, indice)
    else:
        print("\nEscolha um valor Válido.")

