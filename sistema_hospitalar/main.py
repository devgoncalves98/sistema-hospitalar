from sistema import SistemaHospitalar

def menu():
    sistema = SistemaHospitalar()
    while True:
        print("\n--- Menu Principal (CLI) ---")
        print("1. Adicionar paciente")
        print("2. Buscar paciente por CPF")
        print("3. Listar pacientes por prioridade")
        print("4. Exportar dados em XML")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            prioridade = int(input("Prioridade médica (1-10): "))
            sistema.adicionar_paciente(nome, cpf, prioridade)
        elif escolha == '2':
            cpf = input("CPF do paciente: ")
            paciente = sistema.buscar_paciente(cpf)
            if paciente:
                print(paciente)
            else:
                print("Paciente não encontrado.")
        elif escolha == '3':
            sistema.listar_pacientes_por_prioridade()
        elif escolha == '4':
            sistema.exportar_xml("pacientes.xml")
            print("Exportado para pacientes.xml")
        elif escolha == '5':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()