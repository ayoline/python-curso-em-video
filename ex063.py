fib = []
num = int(input('Digite o primeiro numero da sequencia de fibonacci desejada: '))
fib.insert(0, num)
qtd = int(input('Digite a quantidade de numeros da sequência você quer: '))
i = 1
print(f'{fib[0]}',end=' => ')

while(i != qtd):
    if(i == 1):
        fib.insert(i, fib[0])
        print(f'{fib[i]}',end=' => ')
        i += 1
    else:
        fib.insert(i, (fib[i -1] + fib[i -2]))
        print(f'{fib[i]}',end=' => ')
        i += 1
print('FIM')
  
