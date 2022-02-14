'''
Calculating the mean of numbers stored in a file
'''
from statistics import mean


def read_data(filename):
  with open(filename) as f:
    numbers = [float(line) for line in f]
  return numbers

def calculate_mean(numbers):
  s = sum(numbers)
  N = len(numbers)
  mean = s / N
  return mean

# $HOME/local_Document/Programming/DoingMathWithPython/chapter3/3-7-1へcdして実行
if __name__ == '__main__':
  data = read_data('mydata.txt')
  mean = calculate_mean(data)
  print('Mean: {0}'.format(mean))
