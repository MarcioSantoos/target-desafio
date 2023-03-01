def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


fib_sequence = []
value = int(input(print('Digite um valor: ')))
number = fibonacci(value)

for i in range(value):
  fib_sequence.append(fibonacci(i))
  print(fibonacci(i), sep='', end=',')

if value in fib_sequence:
  print('\n O valor ', value,' existe na sequencia')
else:
  print('\n O valor ', value, ' não existe na sequencia')