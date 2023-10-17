def imprimir_produtos(produtos):
    with open('produto.csv',newline='') as produto.csv:

        leitor_csv = csv.reader(produto_csv)
        linhas = list(leitor_csv)
        
    linhas [linha] = novos_dados

    for i,linha in enumerate(linhas):
        if i == 0:
            print(linha)
        Custo = produto['Valor']+(produto['Valor']*produto['Imposto1']+produto['Valor']*produto['Imposto2']+produto['Valor']*produto['Imposto3'])+(produto['Quantidade']/produto['Frete'])
        print(f"{produto['Nome']},{produto['Valor']},{Custo},{produto['Custo']+(Custo*produto['Margem'])},{produto['Quantidade']}")
