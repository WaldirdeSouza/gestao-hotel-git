from clientes import obter_cliente
from quartos import obter_quarto, marcar_ocupado, marcar_disponivel

reservas = []

def criar_reserva(cliente_id, numero_quarto, data_entrada, data_saida):
    """Cria uma nova reserva para um cliente num quarto disponível."""
    cliente = obter_cliente(cliente_id)
    if not cliente:
        print(f"[ERRO] Cliente com ID {cliente_id} não encontrado.")
        return

    quarto = obter_quarto(numero_quarto)
    if not quarto:
        print(f"[ERRO] Quarto {numero_quarto} não existe.")
        return

    if not quarto["disponivel"]:
        print(f"[ERRO] Quarto {numero_quarto} está ocupado.")
        return

    reserva_id = len(reservas) + 1
    reserva = {
        "id": reserva_id,
        "cliente_id": cliente_id,
        "cliente_nome": cliente["nome"],
        "numero_quarto": numero_quarto,
        "data_entrada": data_entrada,
        "data_saida": data_saida,
        "ativa": True
    }
    reservas.append(reserva)
    marcar_ocupado(numero_quarto)
    print(f"[OK] Reserva #{reserva_id} criada: {cliente['nome']} → Quarto {numero_quarto} ({data_entrada} a {data_saida}).")

def cancelar_reserva(reserva_id):
    """Cancela uma reserva existente e liberta o quarto."""
    for r in reservas:
        if r["id"] == reserva_id and r["ativa"]:
            r["ativa"] = False
            marcar_disponivel(r["numero_quarto"])
            print(f"[OK] Reserva #{reserva_id} cancelada. Quarto {r['numero_quarto']} agora disponível.")
            return
    print(f"[ERRO] Reserva #{reserva_id} não encontrada ou já cancelada.")

def listar_reservas():
    """Lista todas as reservas ativas."""
    ativas = [r for r in reservas if r["ativa"]]
    if not ativas:
        print("Não existem reservas ativas.")
        return
    print("\n--- Reservas Ativas ---")
    for r in ativas:
        print(f"Reserva #{r['id']} | {r['cliente_nome']} | Quarto {r['numero_quarto']} | {r['data_entrada']} → {r['data_saida']}")
    print("-----------------------\n")
    print("-----------------------\n")
    print("-----------------------\n")
    print("-----------------------\n")
