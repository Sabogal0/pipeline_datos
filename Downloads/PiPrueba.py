# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 00:11:22 2024

@author: Santiago Sabogal
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

k = 1
s = 0

for i in range(10000000):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
    k += 2     
print(s)

piTable = []
for i in range(1,10):
    a = str(s).count(str(i))
    piTable.append(a)
    data = {"conteo":piTable}

df = pd.DataFrame(data)
df.index = df.index+1
df.sort_values(by=["conteo"],ascending=False, inplace=True)

df.plot.bar()

