#métodos uteis da classe string

curso = " pytHoN "

print (curso.upper()) #letras maiúsculas

print (curso.lower()) #letras menúsculas

print (curso.strip()) #retira os espaços

print (curso.lstrip()) #retira o espaço no inicio - esquerda

print (curso.rstrip()) #retira o espaço no final- direira


print (curso.center(10, "#")) #centraliza colocando a quantidade de caracteres estipulada e coloca entre (#)

print ("." .join(curso)) # junção coloca o valor entre cada letra da variável


#*****Interpolação de variáveis

# %  não é recomendada

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

# %s quando usar strings, %f pontos flutuantes, %d inteiros
print("Olá! Me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


# format


nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá! Me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá! Me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Luiza", "idade": 30}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

#fatiamento de strings

nome = "Guilherme Luis Souza"

print(nome[0])

print(nome[5])

print(nome[5:8:15])

print(nome[:])

print(nome[::-1])


#strings multiplas linhas

nome = "Luiza"

mensagem = f"""Olá meu nome é {nome}, 
estou aprendendo Python!"""

print(mensagem)

print("""
 *********Menu**********
      1- Central
      2- Financeiro
      3- TI
************************
     """)