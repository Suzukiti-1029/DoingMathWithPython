def find_corr_x_y(x, y):
  n = len(x)
  # find the sum of the products
  prod = [xi * yi for xi, yi in zip(x, y)]
  sum_prod_x_y = sum(prod)
  sum_x = sum(x)
  sum_y = sum(y)
  squared_sum_x = sum_x ** 2
  squared_sum_y = sum_y ** 2
  x_square = [xi ** 2 for xi in x]
  # find the sum
  x_square_sum = sum(x_square)
  y_square = [yi ** 2 for yi in y]
  # find the sum
  y_square_sum = sum(y_square)

  # use formula to calculate correlation
  numerator = n*sum_prod_x_y - sum_x*sum_y
  denominator_term1 = n*x_square_sum - squared_sum_x
  denominator_term2 = n*y_square_sum - squared_sum_y
  denominator = (denominator_term1 * denominator_term2) ** 0.5
  correlation = numerator / denominator

  return correlation

def scatter_plot(x, y):
  plt.scatter(x, y)
  plt.xlabel('max_temperature')
  plt.ylabel('daylight_hours')
  plt.show()

# ここから
def read_csv(filename):
  with open(filename, encoding='shift_jis') as f: # shift_jis形式なので指定
    reader = csv.reader(f)
    next(reader)
    max_temp = []
    daylight_hours = []
    for row in reader:
      max_temp.append(float(row[1]))
      daylight_hours.append(float(row[2]))
  return max_temp, daylight_hours

import matplotlib.pyplot as plt
import csv

# mv ./chapter3/3-7-2/data.csv ./ をしてから実行
if __name__ == '__main__':
  max_temp, daylight_hours = read_csv('data.csv')
  corr = find_corr_x_y(max_temp, daylight_hours)
  print('Correlation: {0}'.format(corr))
  scatter_plot(max_temp, daylight_hours)
