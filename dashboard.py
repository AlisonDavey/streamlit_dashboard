import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

def main():
    
    # time selection
    st.sidebar.title("Select time period")
    start_date = st.sidebar.date_input('Start date', min_value = datetime.date(2022,3,11), max_value = datetime.date(2022,3,14), value = datetime.date(2022,3,11))
    start_time = st.sidebar.time_input('Start time', value = datetime.time(16))
    
    end_date = st.sidebar.date_input('End date', min_value = datetime.date(2022,3,11), max_value = datetime.date(2022,3,14), value = datetime.date(2022,3,14))
    end_time = st.sidebar.time_input('End time', value = datetime.time(22))

    start = start_date.strftime("%Y-%m-%d")+'T'+start_time.strftime("%H-%M-%S")
    end = end_date.strftime("%Y-%m-%d")+'T'+end_time.strftime("%H-%M-%S")
    
    # API call
    pipes_api='https://api.tinybird.co/v0/pipes/'
    pipe_mv='events_hour_pipe.csv'
    token_mv='p.eyJ1IjogImEyNGY5NWFhLTM3MzMtNGIyNy05NzVkLWRkYmY4OWExZjMyOSIsICJpZCI6ICJmNWM1NThiMS0zZjA3LTRhYzgtYjQ1Mi04OTgzZTU2ZTk1MDcifQ.Y0D-gimVEfcY1hLpEa66uS0ssSX9JKw2NZW-Nk2cFcg'
    
    url=pipes_api+pipe_mv+"?start_date="+start+"&end_date="+end+"&token="+token_mv
    df=pd.read_csv(url)
    
    # chart
    plot = px.bar(
                data_frame=df,
                x = "hour",
                y = "number",
                color = "event",
                color_discrete_sequence=px.colors.qualitative.T10,
                labels={
                     "hour": "Hour",
                     "event": "Event",
                     "number": "Count"
                 }, height=600)
    
    st.write("Join our [Tinybird](https://www.tinybird.co) [Slack](https://join.slack.com/t/tinybird-community/shared_invite/zt-yi4hb0ht-IXn9iVuewXIs3QXVqKS~NQ) community") 
    st.title('In-Product Dashboard for your user')
    st.header('Events per hour for a single user')
    st.plotly_chart(plot, use_container_width=True)

if __name__ == '__main__':
	main()
