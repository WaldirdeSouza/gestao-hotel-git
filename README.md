# Sistema de Gestão de Reservas de Hotel

## Autor
- Waldir Alves

## Descrição Geral
Sistema desenvolvido em Python para gerir reservas, quartos e clientes de um hotel, com recurso ao Git e GitHub. 
O projeto foi desenvolvido como parte de um trabalho de avaliação focado na utilização de **Git e GitHub** para controlo de versões e organização do trabalho.

## Como Executar

> Requisito: Python 3.x instalado.

```bash
python app.py
```

## Funções Principais do Sistema

### Clientes (`clientes.py`)
- `registar_cliente(nome, email, telefone)` — Adiciona um novo cliente ao sistema
- `listar_clientes()` — Mostra todos os clientes registados
- `obter_cliente(id)` — Devolve os dados de um cliente pelo ID

### Quartos (`quartos.py`)
- `listar_quartos()` — Mostra todos os quartos e o seu estado (disponível/ocupado)
- `listar_quartos_disponiveis()` — Mostra apenas os quartos disponíveis
- `marcar_ocupado(numero)` — Marca um quarto como ocupado
- `marcar_disponivel(numero)` — Liberta um quarto

### Reservas (`reservas.py`)
- `criar_reserva(cliente_id, numero_quarto, data_entrada, data_saida)` — Cria uma nova reserva
- `cancelar_reserva(reserva_id)` — Cancela uma reserva existente e liberta o quarto
- `listar_reservas()` — Mostra todas as reservas ativas

## Estrutura do Projeto

```
gestao-hotel-git/
├── app.py         # Menu principal e ponto de entrada
├── clientes.py    # Gestão de clientes
├── quartos.py     # Gestão de quartos
├── reservas.py    # Gestão de reservas
└── README.md      # Documentação do projeto
```

## Branches Utilizadas

| Branch            | Funcionalidade                        |
|-------------------|---------------------------------------|
| `main`            | Ramo principal (versão estável)       |
| `feature-clientes`| Registo e listagem de clientes        |
| `feature-quartos` | Gestão de quartos disponíveis/ocupados|
| `feature-reservas`| Criação e cancelamento de reservas    |

## Versão
`v1.0` — Versão final do sistema de gestão de hotel

## Contato
hotel1@mail.com