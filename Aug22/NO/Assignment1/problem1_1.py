import numpy as np
from numpy.linalg import norm, inv
import pandas as pd
import matplotlib.pyplot as plt

# time unit: days
# total poplulation: 130 crores
# time horizon of interest: March 23, 2020 to Oct 15, 2020
# removed = recovered + deceased

## 1. get data using pandas
## 2.
## 3. Jacobian matrix, rank, condition number
## 4. Coefficient matrix, rank, condition number
## 5. Cholesky factorization
## 6. estimate beta, gamma, R_0
## 7. use scipy.optimize to estimate beta, gamma, R_0
## 8. observations
## 9. estimate and plot R_0(t)

df = pd.read_csv("state_wise_daily.csv")
df = df[(df['Date_YMD'] > '2020-03-22') & (df['Date_YMD'] < '2020-10-16')]
df['Total'] = df.iloc[:,3:].sum(axis='columns')

df_reduced = df[['Date_YMD', 'Status', 'Total']]
df_reduced.sort_values(by='Date_YMD')

required = pd.DataFrame(
  [],
  columns=['Date_YMD', 'Confirmed', 'Recovered', 'Deceased']
)
for date, group in df_reduced.groupby('Date_YMD'):
  required.loc[len(required.index)] = [
    date,
    group.iloc[0,2],
    group.iloc[1,2],
    group.iloc[2,2],
  ]

# store cumulative sum instead in the dataframe
required['Confirmed'] = required['Confirmed'].cumsum()
required['Recovered'] = required['Recovered'].cumsum()
required['Deceased'] = required['Deceased'].cumsum()

# Initial total population is 130 crores
N = 130 * 100 * 100 * 1000
# make a dataframe for susceptible, infected and recovered
df_SIR = pd.DataFrame(
  [],
  columns=['Date', 'Susceptible', 'Infected', 'Recovered']
)
for index, row in required.iterrows():
  df_SIR.loc[len(df_SIR.index)] = [
    row['Date_YMD'],
    N - row['Confirmed'] - row['Deceased'],
    row['Confirmed'] - row['Recovered'] - row['Deceased'],
    row['Recovered'] + row['Deceased'],
  ]
  
# df_SIR.plot(x='Date', y='Susceptible')
df_SIR.plot(x='Date', y='Infected')
# df_SIR.plot(x='Date', y='Recovered')
plt.show()
