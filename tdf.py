import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# import data
df = pd.read_csv('stages_TDF.csv').dropna()
#df.info()

"""
it appears that a few cells in Winner_Country are null
It appears that the europeans represented a large amount of the stage winners before especially French
"""

# Number of stage wins per top country origin
"""
df['Winner_Country'].value_counts().head(10).plot('bar')
plt.title('Number of stage wins per top country origin')
plt.show()
"""


# Top french winners
"""
FRA = df.loc[(df['Winner_Country']=='FRA')]
FRA['Winner'].value_counts().head(10).plot('bar')
plt.title('Top french winners')
plt.show()
"""

# Number of french stages win per year
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].map(lambda x: x.year)
FRA = df.loc[(df['Winner_Country']=='FRA')]
FRA.groupby('Year').count().plot(kind='bar')
plt.title('Number of Stages by Year')
plt.show()



# Evolution of the proportion of the FRA, BEL, ITA
"""
y =[]
p = []
df = df.dropna()
for year in range(1904,2017):
    y.append(year)
    before = df.loc[(df['Date']<="{}-01-01".format(year))]
    FRA_before = df.loc[(df['Date']<="{}-01-01".format(year)) & (df['Winner_Country']=='FRA')]
    BEL_before = df.loc[(df['Date']<="{}-01-01".format(year)) & (df['Winner_Country']=='ITA')]
    ITA_before = df.loc[(df['Date']<="{}-01-01".format(year)) & (df['Winner_Country']=='BEL')]
    proportion = [len(FRA_before)/len(before), len(BEL_before)/len(before), len(ITA_before)/len(before)]
    p.append(proportion)

plt.plot(y,p)

plt.show()
"""