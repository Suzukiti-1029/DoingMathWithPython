'''
Multiplication table printer
'''
def multi_table(a):
  for i in range(11):
    print('{0} × {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
  a = input('Enter a number: ')
  multi_table(float(a))
