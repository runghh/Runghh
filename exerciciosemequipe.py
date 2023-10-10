
def atualizar_cpntato(contatos,contato,num,nome,email,ID)
    if ID <= len(Produtos) and ID < len(Produtos):
        Produtos[id]['Nome'] = nome
        Produtos[id]['Numero'] = numero
        Produtos[id]['Email'] = email
    else:
        print("ID INVALIDO")
    print("CONTATO ATUALIZADO")

    
while True:
    print("-----AGENDA DE CONTATOS-------")
    print("1 = CADASTRAR CONTATO")
    print("2 = LISTA DE CONTATOS")
    print("3 = ATUALIZAR CONTATO")
    print("4 = DELETAR CONTATO")
    print("5 = ENCERRAR")
    print("-"*30)
    escolha = int(input("escolha uma opção"))

    if escolha == 1:

    elif escolha == 2:

    elif escolha == 3:
        print("------ATUALIZAR CONTATO------")
        ID = int(input("Digite o ID do contato: "))
        nome = str(input("Digite o nome: "))
        numero = int(input("Digite o numero: "))
        email = str(input("Digite o email: "))
        

    elif escolha == 4:

    elif escolha == 5:
        break
    else: 
        ("ESCOLHA INVALIDA!")

    
