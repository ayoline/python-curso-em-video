def fatorial(num, show=False):
  res = 1
  for i in range(2,num +1):
    if show:
      if res == 1:
        print(f'1 x {i}', end=' ')
      elif i == num:
        print(f'x {i} = ', end='')
      else:
        print(f'x {i}', end=' ')
    res *= i
  return res

print(fatorial(10, True))