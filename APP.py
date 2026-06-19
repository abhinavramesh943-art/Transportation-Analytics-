import pandas as pd

df=pd.read_csv("Toronto Island Ferry Tickets.csv")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df=df.sort_values('Timestamp')
print(df.head())


df.isnull().sum()
df=df.dropna()

df=df.drop_duplicates()


df['Hour'] = df['Timestamp'].dt.hour

df['DayOfWeek'] = df['Timestamp'].dt.day_name()

df['Month'] = df['Timestamp'].dt.month

df['Year'] = df['Timestamp'].dt.year

df['Weekend'] = df['DayOfWeek'].isin(
    ['Saturday','Sunday']
    )






df['NetMovement'] = (df['Sales Count'] - df['Redemption Count'])




                                        
import streamlit as st
#)Dashboard Module
#1)Real time KPI

col1,col2,col3 = st.columns(3)

with col1:
  st.metric("Tickets Sold", int(df['Sales Count'].sum()) )                                                                                                                                        
                                                                                                                                                
                                                        
                                           
                                                        