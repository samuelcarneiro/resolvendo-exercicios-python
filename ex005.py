# Exercício 05
# Faça um programa que leia um número e mostre
# ma tela seu sucessor e seu antecessor

numero = int(input('Informe um número: '))

sucessor = numero + 1
antecessor = numero - 1

print('Número informado {}.'.format(numero))
print('Seu antecessor é {}.'.format(antecessor))
print('Seu sucessor é {}.'.format(sucessor))