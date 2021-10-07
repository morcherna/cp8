print("Введите число: ")
try:
 N = int(input())
except ValueError:
 print('Неверно введено число ')
else:
 print('Введите целевую систему счисления: ')
 try:
  a  = int(input())
 except ValueError:
  print('Неверно введена целевая система счисления ')
 else:
  def system2 ():
   b = bin (N)
   return(b)
  def system8 ():
   global N
   result = ''
   while N > 0:
    result = str(N % 8) + result
    N = N // 8 
   if N < 0:
    result = str((0-N) % 8) + result
    N = N // 8
   return(result)
  while a==2 or a==8:
   if a == 2:
    print(system2())
    break
   if a == 8:
    print(system8())
    break
  else:
   print('Неправильно введена система счисления')
   
      
    