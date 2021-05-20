import random

minusculo = 'abcdefghijklmnopqrstuvwxyz'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '@#$%&&*-=+/.[{[}'

junta = minusculo + maiusculo + numeros + simbolos

tamanho = 16

senha = "".join(random.sample(junta, tamanho))

print("Senha Gerada: ", senha)