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

# ---------------------------
# KPI Cards
# ---------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Tickets Sold",
        int(df['Sales Count'].sum())
    )

with col2:
    st.metric(
        "Tickets Redeemed",
        int(df['Redemption Count'].sum())
    )

with col3:
    st.metric(
        "Net Movement",
        int(df['NetMovement'].sum())
    )

peak_hour = df.groupby('Hour')['Sales Count'].mean().idxmax()

st.metric(
    "Peak Hour",
    f"{peak_hour}:00"
)

# ---------------------------
# Interactive Time Series Plot
# ---------------------------

st.subheader("Hourly Ticket Sales Trend")

hourly = df.groupby('Hour')['Sales Count'].mean()

st.line_chart(hourly)

# ---------------------------
# Date and Time Filters
# ---------------------------

st.subheader("Filters")

min_date = df['Timestamp'].min().date()
max_date = df['Timestamp'].max().date()

selected_date = st.date_input(
    "Select Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)

filtered = df[
    df['Timestamp'].dt.date == selected_date
]

selected_hour = st.slider(
    "Hour Range",
    0,
    23,
    (0, 23)
)

filtered = filtered[
    (filtered['Hour'] >= selected_hour[0]) &
    (filtered['Hour'] <= selected_hour[1])
]

# ---------------------------
# Peak vs Off-Peak Comparison
# ---------------------------

st.subheader("Peak vs Off-Peak Analysis")

df['Peak'] = df['Hour'].between(10, 18)

comparison = df.groupby('Peak')['Sales Count'].mean()

st.bar_chart(comparison)

peak_avg = df[df['Peak']]['Sales Count'].mean()
offpeak_avg = df[~df['Peak']]['Sales Count'].mean()

st.write(f"Peak Average Sales: {peak_avg:.0f}")
st.write(f"Off-Peak Average Sales: {offpeak_avg:.0f}")

# ---------------------------
# User Roles
# ---------------------------

role = st.sidebar.selectbox(
    "User Role",
    [
        "Operations Team",
        "Policy Planner",
        "Management"
    ]
)

if role == "Operations Team":
    st.header("Operations Dashboard")
    st.write("Monitor passenger flow and operational demand.")

elif role == "Policy Planner":
    st.header("Policy Analytics")
    st.write("Analyze seasonal and long-term ferry demand trends.")

elif role == "Management":
    st.header("Executive Summary")
    st.write("High-level KPIs and strategic insights.")


monthly = df.groupby('Month')['Sales Count'].mean()
monthly.plot()
plt.show()


df['Rolling1Hour'] = df['Sales Count'].rolling(4).mean()
                                                                                                          
df['Rolling4Hour'] = df['Sales Count'].rolling(16).mean()

peak = df.nlargest(20, 'Sales Count') 
                                                                                                                                                                                            
                                                        
                                           
                                                        