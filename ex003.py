# Exercício 03
# Crie um programa que leia dois números e mostre a soma entre eles

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

soma = n1 + n2

mensagem = 'A soma de {} e {} é {}.'.format(n1, n2, soma)

print(mensagem)
