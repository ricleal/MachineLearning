#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#sns.set()
sns.set(style="ticks", color_codes=True)

# Money spend in adds and sales
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)
print data.head()

#       TV  Radio  Newspaper  Sales
# 1  230.1   37.8       69.2   22.1
# 2   44.5   39.3       45.1   10.4
# 3   17.2   45.9       69.3    9.3
# 4  151.5   41.3       58.5   18.5
# 5  180.8   10.8       58.4   12.9

# Plot:
sns.pairplot(data,
             x_vars=['TV','Radio','Newspaper'],
             y_vars='Sales',
             size=7,
             aspect=1,
             kind='reg') # kind : {‘scatter’, ‘reg’},


## IRIS dafa
iris = sns.load_dataset("iris")
print iris.head()
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa


## IRIS plot1
# Draw scatterplots for joint relationships and histograms for univariate distributions
sns.pairplot(iris)

## IRIS plot2
# Show different levels of a categorical variable by the color of plot elements:
sns.pairplot(iris, hue="species")

plt.show()
