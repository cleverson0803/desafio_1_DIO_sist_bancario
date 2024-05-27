class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []  # Adicionamos um atributo para armazenar as contas bancárias do usuário

class ContaCorrente:
    num_conta = 1

    def __init__(self, agencia, usuario, saldo_inicial=0):
        self.agencia = agencia
        self.num_conta = ContaCorrente.num_conta
        ContaCorrente.num_conta += 1
        self.usuario = usuario
        self.saldo = saldo_inicial  # Adicionamos o atributo saldo à classe ContaCorrente
        self.extrato = []

def saque(*, saldo, valor, extrato, limite=500, numero_saques=0, limite_saques=3):
    if numero_saques >= limite_saques:
        print('Limite máximo de saques diários atingido.')
        return saldo, extrato, numero_saques
    if valor <= 0:
        print('O valor do saque deve ser positivo.')
        return saldo, extrato, numero_saques
    if valor > limite:
        print(f'Limite máximo de saque de R$ {limite:.2f} por transação.')
        return saldo, extrato, numero_saques
    if saldo < valor:
        print('Saldo insuficiente para realizar o saque.')
        return saldo, extrato, numero_saques
    extrato.append(('Saque', valor))
    saldo -= valor
    numero_saques += 1
    print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato):
    if valor <= 0:
        print('O valor do depósito deve ser positivo.')
        return saldo, extrato
    extrato.append(('Depósito', valor))
    saldo += valor
    print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    return saldo, extrato

def extrato(*, saldo, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for operacao, valor in extrato:
            if operacao == "Depósito":
                print(f"Depósito de R$ {valor:.2f}")
            elif operacao == "Saque":
                print(f"Saque de R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

    # Retornar o saldo e o extrato para atualizar a conta, mesmo que não haja movimentações
    return saldo, extrato

def mostrar_extrato(*, saldo, extrato_conta):
    if not extrato_conta:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for operacao, valor in extrato_conta:
            if operacao == "Depósito":
                print(f"Depósito de R$ {valor:.2f}")
            elif operacao == "Saque":
                print(f"Saque de R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

    # Retornar o saldo e o extrato para atualizar a conta, mesmo que não haja movimentações
    return saldo, extrato_conta

def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    if cpf in usuarios:
        print('CPF já cadastrado.')
        return
    usuarios[cpf] = Usuario(nome, data_nascimento, cpf, endereco)
    print(f'Usuário {nome} cadastrado com sucesso.')

def cadastrar_conta_bancaria(contas, agencia, cpf, saldo_inicial=0):
    if cpf not in usuarios:
        print('Usuário não encontrado.')
        return
    usuario = usuarios[cpf]
    if usuario.contas:
        print('Usuário já possui uma conta cadastrada.')
        return
    num_conta = f'{ContaCorrente.num_conta:06d}'
    conta = ContaCorrente(agencia, usuario)
    usuario.contas.append(conta)
    contas[num_conta] = conta
    print(f'Conta bancária {num_conta} cadastrada para o usuário {usuario.nome} com sucesso.')


# Dados iniciais
usuarios = {}
contas = {}
num_conta = None  # Definindo num_conta como variável global e atribuindo None inicialmente

# Menu

numero_saques = 0  # Inicializa o número de saques como zero

while True:
    print("\n--- Menu ---")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Conta Bancária")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do usuário: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, Num - bairro - cidade/estado): ")
        cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

    elif opcao == "2":
        cpf = input("CPF do usuário: ")
        cadastrar_conta_bancaria(contas, '0001', cpf)
        if cpf in usuarios:
            usuario = usuarios[cpf]
            if usuario.contas:
                num_conta = f'{usuario.contas[-1].num_conta:06d}'
                print(f'Conta bancária {num_conta} cadastrada para o usuário {usuario.nome} com sucesso.')
            else:
                print("Usuário não possui conta cadastrada.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "3":
        if num_conta is None:
            print("Nenhuma conta cadastrada.")
            continue
        valor = float(input("Valor do depósito: "))
        if num_conta in contas:
            conta = contas[num_conta]
            conta.saldo, conta.extrato = deposito(conta.saldo, valor, conta.extrato)
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        if num_conta is None:
            print("Nenhuma conta cadastrada.")
            continue
        valor = float(input("Valor do saque: "))
        if num_conta in contas:
            conta = contas[num_conta]
            saldo, extrato, numero_saques = saque(saldo=conta.saldo, valor=valor, extrato=conta.extrato, numero_saques=numero_saques)
            conta.saldo = saldo  # Atualiza o saldo da conta com o novo saldo retornado pela função saque
            conta.extrato = extrato  # Atualiza o extrato da conta com o novo extrato retornado pela função saque
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        if num_conta is None:
            print("Nenhuma conta cadastrada.")
            continue
        if num_conta in contas:
            conta = contas[num_conta]
            conta.saldo, conta.extrato = mostrar_extrato(saldo=conta.saldo, extrato_conta=conta.extrato)
        else:
            print("Conta não encontrada.")


    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
