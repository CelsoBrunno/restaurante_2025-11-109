import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def exibir_nome_do_programa():
    print("""



░█████╗░░█████╗░██████╗░██╗░░░░░██╗███╗░░██╗██╗░░██╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║████╗░██║██║░░██║██╔══██╗██╔════╝
██║░░╚═╝███████║██████╔╝██║░░░░░██║██╔██╗██║███████║██║░░██║╚█████╗░
██║░░██╗██╔══██║██╔══██╗██║░░░░░██║██║╚████║██╔══██║██║░░██║░╚═══██╗
╚█████╔╝██║░░██║██║░░██║███████╗██║██║░╚███║██║░░██║╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═════╝░

██████╗░██╗░░░██╗██████╗░░██████╗░██╗░░░██╗███████╗██████╗░
██╔══██╗██║░░░██║██╔══██╗██╔════╝░██║░░░██║██╔════╝██╔══██╗
██████╦╝██║░░░██║██████╔╝██║░░██╗░██║░░░██║█████╗░░██████╔╝
██╔══██╗██║░░░██║██╔══██╗██║░░╚██╗██║░░░██║██╔══╝░░██╔══██╗
██████╦╝╚██████╔╝██║░░██║╚██████╔╝╚██████╔╝███████╗██║░░██║
╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝j
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Adicionar avaliação')
    print('5. Adicionar item ao cardápio')
    print('6. Exibir cardápio')
    print('7. Sair\n')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    print('Teste')
    nome = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')
    Restaurante(nome, categoria)
    
    print(f'O restaurante {nome.title()} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    if not Restaurante.restaurantes:
        print('Nenhum restaurante cadastrado.')
    else:
        Restaurante.listar_restaurantes()
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado do restaurante')
    nome = input('Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante = Restaurante.buscar_por_nome(nome) 
    
    if restaurante:
        restaurante.alternar_estado()
        status = 'ativado' if restaurante.ativo else 'desativado'
        print(f'O restaurante {restaurante.nome} foi {status} com sucesso!')
    else:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def adicionar_avaliacao():
    exibir_subtitulo('Adicionar avaliação')
    nome = input('Digite o nome do restaurante: ')
    restaurante = Restaurante.buscar_por_nome(nome)
    if restaurante:
        cliente = input('Digite o nome do cliente: ')
        try:
            nota = int(input('Digite a nota (1 a 5): '))
            restaurante.receber_avaliacao(cliente, nota)
            print('Avaliação registrada com sucesso!')
        except ValueError:
            print('Nota inválida. Use um número inteiro de 1 a 5.')
    else:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def adicionar_item_cardapio():
    exibir_subtitulo('Adicionar item ao cardápio')
    nome = input('Digite o nome do restaurante: ')
    restaurante = Restaurante.buscar_por_nome(nome)
    if not restaurante:
        print('O restaurante não foi encontrado.')
        voltar_ao_menu_principal()
        return

    print('1. Prato')
    print('2. Bebida')
    try:
        tipo = int(input('Escolha o tipo (1 ou 2): '))
    except ValueError:
        print('Opção inválida.')
        voltar_ao_menu_principal()
        return

    nome_item = input('Nome do item: ')
    try:
        preco = float(input('Preço (R$): '))
    except ValueError:
        print('Preço inválido.')
        voltar_ao_menu_principal()
        return

    if tipo == 1:
        descricao = input('Descrição do prato: ')
        item = Prato(nome_item, preco, descricao)
    elif tipo == 2:
        tamanho = input('Tamanho (ex: 200ml, 1L): ')
        item = Bebida(nome_item, preco, tamanho)
    else:
        print('Opção inválida.')
        voltar_ao_menu_principal()
        return

    restaurante.adicionar_no_cardapio(item)
    print(f'{nome_item} adicionado ao cardápio de {restaurante.nome}!')
    voltar_ao_menu_principal()

def exibir_cardapio_restaurante():
    exibir_subtitulo('Exibir cardápio')
    nome = input('Digite o nome do restaurante: ')
    restaurante = Restaurante.buscar_por_nome(nome)
    if restaurante:
        restaurante.exibir_cardapio()
    else:
        print('O restaurante não foi encontrado.')
    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Finalizar app')
    print('Até logo!\n')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            adicionar_avaliacao()
        elif opcao == 5:
            adicionar_item_cardapio()
        elif opcao == 6:
            exibir_cardapio_restaurante()
        elif opcao == 7:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
