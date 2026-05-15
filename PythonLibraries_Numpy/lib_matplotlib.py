#Area
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
N=30
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)
area=(30*np.random.rand(N))**2
plt.scatter(x,y,s=area,c=colors,alpha=0.4)
plt.show()
#Graph
from matplotlib import style
style.use('ggplot')
x=[2,4,6]
y=[12,14,16]

x2=[3,5,7]
y2=[7,14,15]

plt.bar(x,y,color='r',align='center')
plt.bar(x2,y2,color='g',align='center')

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()











