#Exercicio 1 - cadastrar produt com qnt imposto e valor, 2- imprimir e 3 fechar
estoquetaxa = []
estoqueqnt = []
estoquecusto = []
estoquevenda = []
estoquevalor = []
estoquenome = []
while True: 
    print("-------------------------------")
    print(" 1= CADASTRAR PRODUTO ")
    print(" 2= IMPRIMIR ESTOQUE ")
    print(" 3= FECHAR ")
    print("-------------------------------")
    escolha = int(input("Escolha uma opção:"))
    if escolha == 1:
        print("------------CADASTRO DE PRODUTOS------------------")
        nome = input("Digite o nome do produto: ")
        valordecusto = int(input("Digite o valor do produto: "))
        estoquevalor.append(valordecusto)
        qnt = int(input("Digite a quantidade de produtos: "))
        
        imposto1 = int(input("Digite a taxa de imposto 1 :"))
        imposto2 = int(input("Digite a taxa de imposto 2 :"))       
        imposto3 = int(input("Digite a taxa de imposto 3 :"))
       
        taxadevenda = int(input("Digite a taxa de lucro:"))
        estoquetaxa.append(taxadevenda)
        taxadevenda = taxadevenda/100
        imposto1 = imposto1/100
        imposto2 = imposto2/100
        imposto3 = imposto3/100 
        valordecusto = (valordecusto+(valordecusto*imposto1)+(valordecusto*imposto2)+(valordecusto*imposto3)+((1/qnt)*qnt))
        valordevenda = qnt*(valordecusto+(valordecusto*taxadevenda))
        estoquenome.append(nome)
        estoqueqnt.append(qnt)
        estoquecusto.append(valordecusto)
        estoquevenda.append(valordevenda)

    elif escolha == 2:
        print("-------------PRODUTOS DISPONIVEIS-----------")
        for i in range(len(estoquecusto)):
    
            print("Produto",estoquenome[i])
            print("Valor sem taxa: R$",estoquevalor[i])
            print(f"Valor com taxas e frete: R$ {estoquecusto[i]:.2f}")
            print("Porcentagem de venda: ",estoquetaxa[i],"%")
            print("Quantidade: ",estoqueqnt[i])
            print(f"Preço unitario do produto: R${estoquevenda[i]/estoqueqnt[i]:.2f}") 
            print("--------------------------------------------------")
    elif escolha == 3:
        break
    else:
        print("ESCOLHA INVALIDA")
        print("----------------------------------------------")