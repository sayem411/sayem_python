import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4), index=list(range(6)), columns=list('ABCD'))
print(df)
print(df.describe())

