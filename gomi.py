import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 制御点を指定 (x, y)
points = np.array([
    [0, 0],
    [1, 2],
    [3, 3],
    [4, 1],
    [5, 4],
    [8, 3]
])

# x, y 座標を分離
x = points[:, 0]
y = points[:, 1]

# 滑らかに補間するための新しい x 値
x_new = np.linspace(x.min(), x.max(), 100)

# Bスプライン補間
spl = make_interp_spline(x, y, k=3)  # 3次のBスプライン (k=3)
y_new = spl(x_new)

# 描画
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ro', label="Control Points")  # 制御点
plt.plot(x_new, y_new, 'b-', label="B-Spline Curve")  # Bスプライン曲線
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("B-Spline Curve Interpolation")
plt.grid()
plt.show()
