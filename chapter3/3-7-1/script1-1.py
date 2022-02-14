# Find the sum of numbers stored in a file
def sum_data(filename):
  s = 0
  with open(filename) as f:
    for line in f:
      s += float(line)
  print('Sum of the numbers: {0}'.format(s))

# $HOME/local_Document/Programming/DoingMathWithPython/chapter3/3-7-1へcdして実行
if __name__ == '__main__':
  sum_data('mydata.txt')
