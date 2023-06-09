import csv
import numpy as np
import matplotlib.pyplot as plt

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
    # 先頭の列を削除
    l = np.delete(l, 0, axis=1)

    # 末尾の空文字の列を削除
    l = np.delete(l, 192, axis=1)

    # 文字列型のnumpy配列をfloat型のnumpy配列に変換
    temperature_data = l.astype(float)

# 1 から 192 までの間を、192等分して、配列にする
x = np.linspace(1, 192, 192)
y = np.linspace(1, 256, 256)
X, Y = np.meshgrid(x, y)

# 三次元グラフの描画
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, temperature_data)

# グラフの表示
plt.show()

# ファイル書き出し
# with open('./result.txt', mode='w') as f:
#   for x in range(192):
#     for y in range(256):
#        f.write(f'x: {x + 1}, y: {y + 1}, value: {temperature_data[y][x]}\n')
