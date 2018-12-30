import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x_vulns, y_vulns,z_vulns = np.loadtxt('vulns.csv', delimiter=',', unpack=True)
x, y,z = np.loadtxt('nonvulns.csv', delimiter=',', unpack=True)

# Axes3D.scatter(x_vulns,y_vulns,z_vulns,zdir='z', s=20,c='red',depthshade=True)
# Axes3D.scatter(x,y,z,zdir='z', s=20,c='blue',depthshade=True)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_vulns, y_vulns, z_vulns, c='r', marker='o')
ax.scatter(x, y, z, c='b', marker='^')

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('# mod files')
ax.set_ylabel('# added lines')
ax.set_zlabel('# removed lines')

ax.set_xlim(0, 20)
ax.set_ylim(0, 500)
ax.set_zlim(0, 500)
# ax.

plt.show()
# plt.plot(x_vulns, y_vulns,z_vulns,'ro')
# plt.plot(x, y,z,'go')
# plt.title('problem space')
# plt.legend()
# plt.show()


