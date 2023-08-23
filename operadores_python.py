#operadores aritiméticos
a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print(a + (a * b))

#operadores de comparação

saldo = 200

saque = 450

print(saldo < saque)

print(saque == saldo)

print(saldo > saque)

print(saldo != saque)

print(saldo >= saque)


#operadores de atribuição
saldo += 200
print(saldo)
saldo -= 300
print(saldo)

saldo *= 2
print(saldo)

saldo /= 5
print(saldo)

saldo %= 20
print(saldo)

saldo = 500
print(saldo)

saldo //= 2
print(saldo)

saldo *= 10
print(saldo)

saldo **= 2
print(saldo)


#operadores logicos

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
print(saldo >= saque and saque <= limite)

saldo >= saque or saque <= limite
print(saldo >= saque or saque <= limite)

not saldo >= saque 
print(not saldo >= saque )

#operadores de identidade

saldo = 1000
limite = 50

print(saldo is limite)
print(saldo is not limite)

#operadores de associação

frutas = ["limao", "laranja"]
print("uva" in frutas)

print("laranja" in frutas)

print("limao" not in frutas)
