# Exercício 4
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele

info = input('Informe alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(info))
print('Só tem espaços? ', info.isspace())
print('É um número? ', info.isnumeric())
print('É alfabético?', info.isalpha())
print('É alfanumérico? ', info.isalnum())
print('Está em maiúsculas? ', info.isupper())
print('Está em minúsculas? ', info.islower())
print('Está capitalizada? ', info.istitle())
