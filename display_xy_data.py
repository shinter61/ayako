import csv
import numpy as np

temperature_data = []

with open('./0517_170409.csv') as f:
  reader = csv.reader(f)

  # l に csv の中身が二次元配列で入る
  l = [row for row in reader]

  # 上から4行削除
  for _i in range(4):
    l.pop(0)

  l = np.array(l)

  # axis = 1 なら列を削除
  temperature_data = np.delete(l, 0, axis=1)

with open('./result.txt', mode='w') as f:
  for x in range(192):
    for y in range(256):
       f.write(f'x: {x + 1}, y: {y + 1}, value: {temperature_data[y][x]}\n')
