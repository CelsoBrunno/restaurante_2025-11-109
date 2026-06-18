from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._cardapio = []
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def alternar_estado(self):
        self._ativo = not self._ativo

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def buscar_por_nome(cls, nome):
        nome_busca = nome.strip().lower()
        for r in cls.restaurantes:

            if r._nome.lower() == nome_busca:
                return r
        return None

    @classmethod
    def listar_restaurantes(cls):
       
        print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(10)} | Status")
        for i in cls.restaurantes:

            status = 'ativado' if i._ativo else 'desativado'
            print(f'{i._nome.ljust(22)} | {i._categoria.ljust(20)} | {str(i.media_avaliacao).ljust(10)} | {status}')
 
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
 
    @property
    def media_avaliacao(self):

        if not self._avaliacao: 
            return 0.0

        soma_das_notas = 0
        for i in self._avaliacao:
            soma_das_notas += i.nota
            
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media


    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):

            self._cardapio.append(item)

    def exibir_cardapio(self):

        print(f'\nCardápio do restaurante {self._nome}\n')
        

        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Descrição: {item.descricao}'
                print(mensagem)
            else:
                mensagem = f'{i}. Nome: {item.nome} | Preço: R${item.preco} | Tamanho: {item.tamanho}'
                print(mensagem)
