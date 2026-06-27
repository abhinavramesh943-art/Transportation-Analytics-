# Transportation-Analytics-

Real Time Ferry Ticket Sales and Redemption Analytics for Toronto Island Park

Internship Project Report

Submitted by

Name: Abhinav Ramesh (One Year Program)

Domain: Machine Learning 

Sub Domain: Transportation Analytics 

Organization: Unified Mentor



Abstract:

Toronto Island Park is one of Toronto's most popular recreational destinations, served by year-round ferry services operating from the Jack Layton Ferry Terminal to Centre Island, Hanlan's Point, and Ward's Island. Efficient ferry operations require continuous monitoring of passenger demand and movement to ensure adequate staffing, scheduling, and congestion management.

This project analyzes historical ferry ticket sales and redemption data recorded at 15-minute intervals between 2015 and 2025. Using Python, Pandas, and Streamlit, an interactive analytics dashboard was developed to identify passenger demand trends, peak travel periods, and net passenger movement. The dashboard provides operational insights that support data-driven decision-making for ferry scheduling and public service planning.


1. Introduction:

Toronto Island ferry services transport thousands of passengers throughout the year. Ticket sales and redemption records contain valuable information regarding passenger inflow, outflow, and demand patterns.

Although these records are continuously generated, there is no centralized analytics platform that provides operational insights in an interactive manner.

This project develops a comprehensive transportation analytics solution capable of:

- Monitoring ticket sales
- Tracking passenger movement
- Identifying peak demand periods
- Supporting operational planning
- Improving passenger experience


2. Problem Statement:

Although ferry ticket transactions are recorded every fifteen minutes, decision-makers currently lack an integrated analytics system capable of:

- Identifying peak passenger flow windows
- Tracking net passenger movement
- Supporting operational planning
- Monitoring seasonal demand changes
- Visualizing transportation trends interactively


3. Objectives:

3.1 Primary Objectives:

- Analyze historical ferry ticket sales and redemption data.
- Identify peak and off-peak travel periods.
- Calculate passenger inflow and outflow.
- Develop a real-time analytics dashboard.

3.2 Secondary Objectives:

- Improve ferry scheduling.
- Reduce congestion.
- Support operational decision-making.
- Assist policy planners using historical trends.


4. Dataset Description:

Column         | Description
_id            | Unique ticket record
Timestamp      | Date and time of transaction
Sales Count    | Number of ferry tickets sold Redemption Count| Number of ferry   tickets            
                  redeemed


5. Analytical Methodology:

https://colab.research.google.com/drive/1RGzQDcd1KPUXnS5kzKFvqFtFboLe5Llp?hl=en#scrollTo=5p44HiJbIVtx


5.1 Data Ingestion:

The dataset was imported into Python using Pandas.

The Timestamp column was converted into datetime format for time-series analysis.

Finally, the records were sorted chronologically.

Output:

- Successfully loaded CSV dataset
- Datetime conversion completed
- Chronological ordering verified


5.2 Data Cleaning:

The following preprocessing operations were performed:

- Missing value detection
- Duplicate removal
- Data consistency verification
- Outlier detection using boxplots

Output:

- No missing timestamps detected
- Duplicate records removed
- Dataset validated for analysis


5.3 Feature Engineering:

Several additional variables were generated from the Timestamp column.

Features Created

- Hour of Day
- Day of Week
- Month
- Season
- Weekend vs Weekday
- Net Passenger Movement

Net Passenger Movement was calculated as:

Net Movement = Sales Count − Redemption Count

These features enabled detailed transportation demand analysis.


6. Exploratory Data Analysis (EDA):

6.1 Hourly Demand Trend:

Average ticket sales were calculated for every hour.

Purpose:

- Identify peak operating hours.
- Understand passenger demand distribution.


6.2 Daily Demand Trend:

Passenger demand was analyzed across all weekdays.

Purpose:

- Compare weekday and weekend demand.


6.3 Seasonal Analysis:

Monthly demand was grouped into four seasons.

Purpose:

- Identify seasonal transportation patterns.
- Estimate off-season utilization.


6.4 Sales vs Redemption Distribution:

Sales and redemption frequencies were compared.

Purpose:

- Measure passenger movement.
- Detect operational imbalance.


6.5 Rolling Average Analysis:

Rolling averages were calculated using:

- 1-hour window (4 intervals)
- 4-hour window (16 intervals)

Purpose:

- Smooth short-term fluctuations.
- Identify long-term demand trends.


7. Key Performance Indicators (KPIs):

The dashboard calculates the following operational KPIs:

7.1 Tickets Sold per Hour:

Measures hourly passenger demand.


7.2 Tickets Redeemed per Hour:

Measures hourly passenger departures.


7.3 Net Passenger Movement:

Difference between ticket sales and ticket redemption.

Net Movement = Sales − Redemption


7.4 Peak Demand Window:

Identifies the hour with maximum average ticket sales.


7.5 Off-Season Utilization Index:

Measures passenger demand during non-peak seasons relative to peak seasons.


8. Streamlit Dashboard:

The project includes an interactive Streamlit dashboard.

8.1 Dashboard Modules:

- KPI Cards
- Interactive Line Charts
- Date Filter
- Hour Filter
- Peak vs Off-Peak Comparison
- Passenger Trend Analysis


8.2 User Roles:

The dashboard supports three user categories.

8.2.1 Operations Team:

Displays:

- Tickets Sold
- Net Passenger Movement
- Peak Hour
- Operational Charts

Purpose:

Daily ferry operation monitoring.


8.2.2 Policy Planner:

Displays:

- Seasonal Trends
- Monthly Analysis
- Weekend vs Weekday Demand

Purpose:

Long-term transportation planning.


8.2.3 Management:

Displays:

- Executive KPIs
- Operational Summary
- Recommendations

Purpose:

Strategic decision-making.

8.3 Streamlit Dashboard:
https://share.google/xLRa2rXGhrTsV97oV


9. Key Insights:

The analysis revealed several important transportation trends.

- Passenger demand is concentrated during specific peak hours.
- Weekend ferry demand is generally higher than weekday demand.
- Summer months exhibit greater passenger traffic than off-season months.
- Ticket redemption closely follows ticket sales, indicating efficient passenger movement.
- Rolling averages reveal recurring demand patterns useful for forecasting.


10. Recommendations:

Based on the analysis, the following recommendations are proposed:

1. Increase ferry frequency during identified peak demand windows.
2. Deploy additional operational staff during high-demand periods.
3. Improve queue management during weekends and holidays.
4. Use historical trends for seasonal scheduling.
5. Monitor off-season utilization to optimize operational costs.
6. Continue collecting near real-time ticket data for ongoing monitoring.


11.Executive Summary:

This project analyzed historical ferry ticket sales and redemption data for Toronto Island Park to identify passenger demand patterns, peak travel periods, and operational trends. The analysis supports data-driven decision-making for ferry scheduling, staffing, and congestion management.

Key Findings:

- Passenger demand is concentrated during specific peak hours, particularly during daytime operating periods.
- Summer months exhibit significantly higher ticket sales compared to off-season months.
- Weekend demand exceeds weekday demand, indicating increased recreational travel.
- Ticket redemption patterns closely follow ticket sales trends, providing insight into passenger movement between the terminal and island destinations.
- Rolling average analysis reveals recurring demand cycles that can assist in operational forecasting.

Operational Implications:

- Increase ferry frequency during identified peak demand windows.
- Allocate additional staff during high-traffic periods to improve passenger flow.
- Maintain efficient service levels during off-season periods while optimizing operational costs.
- Use historical demand patterns to support long-term planning and resource allocation.

Expected Benefits:

- Reduced passenger congestion at ferry terminals.
- Improved scheduling efficiency.
- Better allocation of operational resources.
- Enhanced passenger experience through data-driven service planning.

Conclusion:

The Streamlit dashboard and supporting analytics framework provide a practical decision-support tool for ferry operations, policy planning, and management stakeholders. The solution enables continuous monitoring of passenger demand and supports evidence-based operational improvements.


12. Expected Impact:

Implementation of this analytics system can provide:

- Improved ferry scheduling
- Reduced passenger congestion
- Better staff allocation
- Data-driven operational planning
- Improved passenger experience
- Enhanced government decision support


13. Technologies Used:

- Python
- Pandas
- NumPy
- Streamlit
- Google Colab
- GitHub
- Streamlit Community Cloud


14. Conclusion:

This project successfully demonstrates how transportation analytics can improve ferry operations through data-driven insights. Historical ticket sales and redemption records were transformed into meaningful operational metrics using Python and visualized through an interactive Streamlit dashboard.

The proposed analytics system enables operations teams, policy planners, and management stakeholders to monitor passenger demand, identify peak travel periods, optimize ferry scheduling, and improve overall service efficiency. The project highlights the practical application of data analytics in supporting smarter transportation planning for Toronto Island Park.


15. Reference:

15.1 Toronto Island Ferry Tickets dataset.
