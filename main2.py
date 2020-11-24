import pandas as pd # 引用套件並縮寫為 pd  
df = pd.read_csv('DF3633-1024x20 (Frame 1602837089).csv')
df2 = df[['Point:0','Point:1','Point:2','Intensity']]
X=df2['Point:0']
Y=df2['Point:1']
Z=df2['Point:2']
Value=df2['Intensity']
print(Value)
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(X, Y, Z, c=Value, lw=0, s=1)
plt.show()
