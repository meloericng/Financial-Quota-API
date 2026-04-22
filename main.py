from InsertTicker import InserirCotacao

opcao = input('1-INSERIR COTAÇÃO | 2-DELETAR COTAÇÃO:' )

if opcao == '1':
    print('INSERIR COTAÇÃO')
    InserirCotacao().executar()
else:
    print('DELETAR COTAÇÃO')