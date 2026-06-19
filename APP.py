import pandas as pd

df=pd.read_csv("Toronto Island Ferry Tickets.csv")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.sort_values('Timestamp')

print(df.head())




df.isnull().sum()

df = df.dropna()


df = df.drop_duplicates()


import matplotlib.pyplot as plt

plt.boxplot(df['Sales Count'])
plt.show()






df['Hour'] = df['Timestamp'].dt.hour

df['DayOfWeek'] = df['Timestamp'].dt.day_name()

df['Month'] = df['Timestamp'].dt.month

df['Year'] = df['Timestamp'].dt.year

df['Weekend'] = df['DayOfWeek'].isin(
    ['Saturday','Sunday']
    )






df['NetMovement'] = (df['Sales Count'] - df['Redemption Count'])





hourly_sales = df.groupby('Hour')['Sales Count' ].mean()


hourly_redemption = df.groupby('Hour')['Redemption Count' ].mean()




import matplotlib.pyplot as plt
hourly_sales.plot(figsize=(10,5))              
plt.title("Average Ticket Sales by Hour")   
plt.show()


df.groupby('Weekend')['Sales Count'].mean()


import streamlit as st






monthly = df.groupby('Month')['Sales Count'].mean()
monthly.plot()
plt.show()


df['Rolling1Hour'] = df['Sales Count'].rolling(4).mean()
                                                                                                          
df['Rolling4Hour'] = df['Sales Count'].rolling(16).mean()

peak = df.nlargest(20, 'Sales Count') 
                                                                                                                                                                                            
                                                        
                                           
                                                        