#if

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# if/else

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

# if/elif/else

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    sys.exit("Opção inválida!")


MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")
if idade < MAIOR_IDADE: 
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")
else: 
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")
elif MAIOR_IDADE > idade >= IDADE_ESPECIAL:
    print("Pode fazer apenas as aulas teóricas!")
else: 
    print("Ainda não pode tirar a CNH.")

#estrutura condicional aninhada

conta_normal = True
conta_universitaria = False
conta_especial = False

saldo = 2000
saque = 35500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque! Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!") 
elif conta_especial:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("O sistema não reconhece seu tipo de conta! Entre em contato com seu gerente.")

# Estrutura condicional ternaria

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

