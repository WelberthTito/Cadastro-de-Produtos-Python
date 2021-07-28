from operator import itemgetter # importa o Método para Ordenar pela chave codigo

estoquecomp = [] #Lista que Vai conter o Dicionário.
estoque = {} #Dicionário que vai armazenar os produtos cadastrados
listaordenada = [] = estoquecomp

while True: # Laço que mantem o programa em loop infinito até que seja interrompido.
    print('*****Sistema de cadastro de produtos*****') #Apresentação do  programa
    print('Atenção!!! O codigo "0" Encerra o programa!!!' ) # Aviso:
    estoque['codigo'] = (input('Digite o codigo do Produto: ')) #Armazena o codigo do produto dentro do dicionário estoque
    if estoque['codigo']=='0': #Se o código do produto for igual a string '0', o programa encerra.
        print('Encerrando o programa...')
        break #'LOOP INFINITO' interrompido
    estoque['estoque'] = (input('Digite o numero de produtos no estoque: '))#Armazena o estoque do produto dentro do dicionário estoque
    estoque['minimo'] = (input('Digite o numero minimo de produtos no estoque: '))#Armazena o o minimo do produto dentro do dicionário estoque
    estoquecomp.append(estoque.copy()) #o dicionário estoque é adicionado e copiado para dentro da lista 'estoquecomp'
    x = input('Deseja continuar?' '1 / 0') #A variável x serve para continuar ou não o recebimento de valores.
    if x == '1': # Se a opção for a string '1'
        continue #O laço continua verdadeiro, e o programa se repete
    elif x == '0': # Se a opção for a string '0'
        print('******Lista de produtos:******{} '.format(estoquecomp)) #É impressa a lista com o dicionário de produtos cadastrados.

        y = input('Deseja ordenar a lista? 1/0') #a lista pode ser ordenada em ordem crescente de código de produto.
        if y == '1':
         listaordenada = sorted(listaordenada, key=itemgetter('codigo'))
         print('******Lista de produtos ordenada por código:******{} '.format(listaordenada))

        elif y == '0': # Se não desejar ordenar a lista, o programa vai encerrar.
         print('Encerrando o programa...')
        break
