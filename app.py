from clientes import registar_cliente, listar_clientes
from quartos import listar_quartos, listar_quartos_disponiveis
from reservas import criar_reserva, cancelar_reserva, listar_reservas


def menu():
    print("\n========================================")
    print("   Sistema de Gestão de Reservas Hotel  ")
    print("========================================")
    print(" 1. Registar cliente")
    print(" 2. Listar clientes")
    print(" 3. Ver quartos")
    print(" 4. Ver quartos disponíveis")
    print(" 5. Criar reserva")
    print(" 6. Cancelar reserva")
    print(" 7. Listar reservas ativas")
    print(" 0. Sair")
    print("========================================")
    return input("Opção: ").strip()


def main():
    print("Bem-vindo ao Sistema de Gestão de Reservas de Hotel!")

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do cliente: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            registar_cliente(nome, email, telefone)

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            listar_quartos()

        elif opcao == "4":
            listar_quartos_disponiveis()

        elif opcao == "5":
            listar_clientes()
            try:
                cliente_id = int(input("ID do cliente: "))
                listar_quartos_disponiveis()
                numero_quarto = int(input("Número do quarto: "))
                data_entrada = input("Data de entrada (ex: 2026-04-01): ").strip()
                data_saida = input("Data de saída (ex: 2026-04-05): ").strip()
                criar_reserva(cliente_id, numero_quarto, data_entrada, data_saida)
            except ValueError:
                print("[ERRO] Valor inválido.")

        elif opcao == "6":
            listar_reservas()
            try:
                reserva_id = int(input("ID da reserva a cancelar: "))
                cancelar_reserva(reserva_id)
            except ValueError:
                print("[ERRO] Valor inválido.")

        elif opcao == "7":
            listar_reservas()

        elif opcao == "0":
            print("Até breve!")
            break

        else:
            print("[ERRO] Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
