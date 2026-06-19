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

with col2:
   st.metric("Tickets Redeemed", int(df['Redemption Count'].sum()) )

with col3:
  st.metric("Net Movement", int(df['NetMovement'].sum()) )

peak_hour= df.groupby('Hour')['Sales Count'].mean().idxmax()

st.metric("Peak Hour", f"{peak_hour}:00")

#2)Interactive time series plot 

hourly=df.groupby('Hour')['Sales Count'].mean()

st.line_chart(hourly)

                                                                                                                                 
                                                                                                                                                
                                                        
                                           
                                                        