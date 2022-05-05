from ctypes.wintypes import PINT


num = int(input('Digite um numero qualquer: '))

print(f'O numero {num}, em binário é:{num:08b}')
print(f'O numero {num}, em octal é: {oct(num)}')
print(f'O numero {num}, em hexadecimal é: {hex(num)}')