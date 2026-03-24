quartos = [
    {"numero": 101, "tipo": "Single", "preco": 50.0, "disponivel": True},
    {"numero": 102, "tipo": "Single", "preco": 50.0, "disponivel": True},
    {"numero": 201, "tipo": "Double", "preco": 80.0, "disponivel": True},
    {"numero": 202, "tipo": "Double", "preco": 80.0, "disponivel": True},
    {"numero": 301, "tipo": "Suite",  "preco": 150.0, "disponivel": True},
]

def listar_quartos():
    """Lista todos os quartos e o seu estado."""
    print("\n--- Lista de Quartos ---")
    for q in quartos:
        estado = "Disponível" if q["disponivel"] else "Ocupado"
        print(f"Quarto {q['numero']} | {q['tipo']} | {q['preco']:.2f}€/noite | {estado}")
    print("------------------------\n")

def listar_quartos_disponiveis():
    """Lista apenas os quartos disponíveis."""
    disponiveis = [q for q in quartos if q["disponivel"]]
    if not disponiveis:
        print("Não há quartos disponíveis de momento.")
        return []
    print("\n--- Quartos Disponíveis ---")
    for q in disponiveis:
        print(f"Quarto {q['numero']} | {q['tipo']} | {q['preco']:.2f}€/noite")
    print("---------------------------\n")
    return disponiveis

def obter_quarto(numero):
    """Devolve um quarto pelo número, ou None se não existir."""
    for q in quartos:
        if q["numero"] == numero:
            return q
    return None

def marcar_ocupado(numero):
    """Marca um quarto como ocupado."""
    quarto = obter_quarto(numero)
    if quarto:
        quarto["disponivel"] = False

def marcar_disponivel(numero):
    """Marca um quarto como disponível."""
    quarto = obter_quarto(numero)
    if quarto:
        quarto["disponivel"] = True
