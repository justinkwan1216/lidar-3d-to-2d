import numpy as np
import pandas as pd

from pyntcloud import PyntCloud

import pandas as pd # 引用套件並縮寫為 pd  
df = pd.read_csv('DF3633-1024x20 (Frame 1602837089).csv')
df2 = df[['Point:0','Point:1','Point:2','Intensity']]
X=df2['Point:0']
Y=df2['Point:1']
Z=df2['Point:2']
Value=0*df2['Intensity']/255

d = {'x': X,'y': Y,'z': Z, 
             'red' : Value, 'green' : Value, 'blue' : Value}
        
cloud = PyntCloud(pd.DataFrame(data=d))
cloud.to_file("output.ply")
