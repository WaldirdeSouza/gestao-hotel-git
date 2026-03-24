clientes = []

def registar_cliente(nome, email, telefone):
    """Regista um novo cliente no sistema."""
    for c in clientes:
        if c["email"] == email:
            print(f"[ERRO] Já existe um cliente com o email '{email}'.")
            return

    cliente = {
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email,
        "telefone": telefone
    }
    clientes.append(cliente)
    print(f"[OK] Cliente '{nome}' registado com sucesso (ID: {cliente['id']}).")

def listar_clientes():
    """Lista todos os clientes registados."""
    if not clientes:
        print("Não existem clientes registados.")
        return
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"ID: {c['id']} | Nome: {c['nome']} | Email: {c['email']} | Tel: {c['telefone']}")
    print("-------------------------\n")
    print("-------------------------\n")
def obter_cliente(cliente_id):
    """Devolve um cliente pelo seu ID, ou None se não existir."""
    for c in clientes:
        if c["id"] == cliente_id:
            return c
    return None
