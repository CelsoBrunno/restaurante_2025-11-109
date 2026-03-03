# Epic: Sistema de Gestão de Restaurantes (CLI)

| Campo | Valor |
|-------|-------|
| **Epic ID** | SGR-001 |
| **Prioridade** | Alta |
| **Estimativa** | 1 sprint |

---

## Visão Geral

Sistema em Python para gestão de restaurantes via terminal: cadastro, cardápio, avaliações e controle de status. Sem banco de dados, dados em memória.

---

## User Stories

### US-01 - Cadastro de Restaurantes

**Como** usuário do sistema  
**Quero** cadastrar restaurantes com nome e categoria  
**Para** manter o cadastro da rede

**Critérios de aceite:**
- [ ] Input de nome e categoria
- [ ] Novo restaurante sempre inicia desativado
- [ ] Mensagem de confirmação após cadastro

---

### US-02 - Listagem de Restaurantes

**Como** usuário do sistema  
**Quero** listar todos os restaurantes  
**Para** visualizar nome, categoria, média de avaliação e status

**Critérios de aceite:**
- [ ] Exibir: nome | categoria | avaliação | status (ativado/desativado)
- [ ] Tratar lista vazia

---

### US-03 - Alternar Status do Restaurante

**Como** usuário do sistema  
**Quero** alternar o status de um restaurante (ativado/desativado)  
**Para** controlar quais estão em operação

**Critérios de aceite:**
- [ ] Busca por nome do restaurante
- [ ] Alternar status (ativado ↔ desativado)
- [ ] Mensagem de sucesso ou "restaurante não encontrado"

---

### US-04 - Adicionar Avaliação

**Como** usuário do sistema  
**Quero** registrar avaliação (cliente + nota) em um restaurante  
**Para** acompanhar a satisfação dos clientes

**Critérios de aceite:**
- [ ] Input: nome do cliente, nota (1-5)
- [ ] Rejeitar nota fora do intervalo
- [ ] Calcular e exibir média das avaliações na listagem

---

### US-05 - Adicionar Item ao Cardápio

**Como** usuário do sistema  
**Quero** adicionar pratos e bebidas ao cardápio de um restaurante  
**Para** manter o cardápio atualizado

**Critérios de aceite:**
- [ ] Prato: nome, preço, descrição
- [ ] Bebida: nome, preço, tamanho
- [ ] Busca do restaurante por nome
- [ ] Validação de preço (numérico)

---

### US-06 - Exibir Cardápio

**Como** usuário do sistema  
**Quero** visualizar o cardápio de um restaurante  
**Para** conferir pratos e bebidas disponíveis

**Critérios de aceite:**
- [ ] Busca por nome do restaurante
- [ ] Exibir itens numerados com nome, preço e atributo específico (descrição ou tamanho)

---

### US-07 - Menu Principal e Fluxo de Execução

**Como** usuário do sistema  
**Quero** um menu que permaneça em execução até eu escolher sair  
**Para** realizar várias operações sem reiniciar o programa

**Critérios de aceite:**
- [ ] Menu com as 7 opções (incluindo Sair)
- [ ] Loop contínuo até opção Sair
- [ ] Retorno ao menu após cada operação
- [ ] Tratamento de opção inválida (sem crash)

---

## Especificação Técnica

| Item | Especificação |
|------|---------------|
| **Stack** | Python 3 |
| **Interface** | CLI (terminal) |
| **Persistência** | Em memória |

### Modelo de dados

```
Restaurante: nome, categoria, ativo (bool), cardapio[], avaliacao[]
ItemCardapio (base): nome, preco
  └── Prato: descricao
  └── Bebida: tamanho
Avaliacao: cliente, nota (1-5)
```

### Estrutura sugerida

```
/
├── app.py              # Entry point + menu
└── modelos/
    ├── restaurante.py
    ├── avaliacao.py
    └── cardapio/
        ├── item_cardapio.py
        ├── prato.py
        └── bebida.py
```

---

## Definition of Done

- [ ] Código em repositório versionado
- [ ] Execução sem erros no fluxo principal
- [ ] Tratamento de inputs inválidos
- [ ] Estrutura de pastas conforme especificado

---

## Referência de Menu

1. Cadastrar restaurante
2. Listar restaurantes
3. Alternar estado do restaurante
4. Adicionar avaliação
5. Adicionar item ao cardápio
6. Exibir cardápio
7. Sair
