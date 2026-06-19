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


monthly = df.groupby('Month')['Sales Count'].mean()
monthly.plot()
plt.show()


df['Rolling1Hour'] = df['Sales Count'].rolling(4).mean()
                                                                                                          
df['Rolling4Hour'] = df['Sales Count'].rolling(16).mean()

peak = df.nlargest(20, 'Sales Count')                                                                                                                                                                                             
                                                        
                                           
                                                        import streamlit as st
                                                            #Dashboard Modules
                                                            #1) Real time KPI cards
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

                                                                                                                                            #2) Interactive time series plot
                                                                                                                                            hourly = df.groupby('Hour')['Sales Count'].mean()

                                                                                                                                            st.line_chart(hourly)

                                                                                                                                            #3) Date and Time filters
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
                                                                                                                                                                    "Hour",
                                                                                                                                                                        0,
                                                                                                                                                                            23,
                                                                                                                                                                                (0,23)
                                                                                                                                                                                )

                                                                                                                                                                                filtered = filtered[
                                                                                                                                                                                    (filtered['Hour'] >= selected_hour[0]) &
                                                                                                                                                                                        (filtered['Hour'] <= selected_hour[1])
                                                                                                                                                                                        ]

                                                                                                                                                                                        #4)Peak vs off peak comparison
                                                                                                                                                                                        # Create categories
                                                                                                                                                                                        df['Peak'] = df['Hour'].between(10,18)

                                                                                                                                                                                        # Analysis
                                                                                                                                                                                        comparison = df.groupby('Peak')[
                                                                                                                                                                                            'Sales Count'
                                                                                                                                                                                            ].mean()

                                                                                                                                                                                            st.bar_chart(comparison)

                                                                                                                                                                                            #Display
                                                                                                                                                                                            peak_avg = df[df['Peak']]['Sales Count'].mean()

                                                                                                                                                                                            offpeak_avg = df[~df['Peak']]['Sales Count'].mean()

                                                                                                                                                                                            st.write(
                                                                                                                                                                                                f"Peak average sales: {peak_avg:.0f}"
                                                                                                                                                                                                )

                                                                                                                                                                                                st.write(
                                                                                                                                                                                                    f"Off-peak average sales: {offpeak_avg:.0f}"
                                                                                                                                                                                                    )

                                                                                                                                                                                                    #User Roles

                                                                                                                                                                                                    role = st.sidebar.selectbox(
                                                                                                                                                                                                        "User Role",
                                                                                                                                                                                                            [
                                                                                                                                                                                                                    "Operations Team",
                                                                                                                                                                                                                            "Policy Planner",
                                                                                                                                                                                                                                    "Management"
                                                                                                                                                                                                                                        ]
                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                        #1)Operations Team roles
                                                                                                                                                                                                                                        if role == "Operations Team":
                                                                                                                                                                                                                                            st.header("Operations Dashboard")

                                                                                                                                                                                                                                            #2)Policy Planner views
                                                                                                                                                                                                                                            if role == "Policy Planner":
                                                                                                                                                                                                                                                st.header("Policy Analytics")

                                                                                                                                                                                                                                                #3) Management View
                                                                                                                                                                                                                                                if role == "Management":
                                                                                                                                                                                                                                                    st.header("Executive Summary")