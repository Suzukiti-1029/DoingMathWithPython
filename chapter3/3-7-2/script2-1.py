import csv
import matplotlib.pyplot as plt

def scatter_plot(x, y):
  plt.scatter(x, y)
  plt.xlabel('Number')
  plt.ylabel('Square')
  plt.show()

def read_csv(filename):
  numbers = []
  squared = []
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      numbers.append(int(row[0]))
      squared.append(int(row[1]))
  return numbers, squared

# $HOME/local_Document/Programming/DoingMathWithPythonへnumbers.csvを移動して実行
# mv ./chapter3/3-7-2/numbers.csv ./
if __name__ == '__main__':
  numbers, squared = read_csv('numbers.csv')
  scatter_plot(numbers, squared)
