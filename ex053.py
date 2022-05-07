import string


def my_function(x):
  return x[::-1]

frase = input('Digite um frase qualqer: ')
frase = frase.replace(" ","")
print(frase)

frase2 = my_function(frase)
print(frase2)

if(frase == frase2):
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')