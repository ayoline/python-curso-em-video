from curses.ascii import isalpha


something = input('Digite algo: ')
print(type(something))
print(f'É numerico? {something.isnumeric()}')
print(f'É string? {something.isalpha()}')

mytuple = (1,2)
print(type(mytuple))