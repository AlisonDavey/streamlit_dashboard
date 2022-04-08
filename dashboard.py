import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

import plotly.graph_objects as go


def main():
    
    st.title('In-Product Dashboard for your user')
    st.header('Events per hour for a single user')
    
    # time selection
    
    add_sidebar = st.sidebar.selectbox('All events or single event type', ('All events','Single event type'))
    if add_sidebar == 'Single event type':  
        event=st.sidebar.selectbox('Single event type', ('AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK'))
    
    dates = st.sidebar.slider('Date range:', 
                               value=(datetime.date(2022,3,11), datetime.date(2022,3,14)),
                               min_value = datetime.date(2022,3,11),
                               max_value = datetime.date(2022,3,11))

    times = st.sidebar.slider('Time range:', 
                               value=(datetime.time(0), datetime.time(23)))
    
    start = dates[0].strftime("%Y-%m-%d")+'T'+times[0].strftime("%H-%M-%S")
    end = dates[1].strftime("%Y-%m-%d")+'T'+times[1].strftime("%H-%M-%S")
    
    st.sidebar.write("Join our [Tinybird](https://www.tinybird.co) [Slack](https://join.slack.com/t/tinybird-community/shared_invite/zt-yi4hb0ht-IXn9iVuewXIs3QXVqKS~NQ) community") 
    

    # API call
    pipes_api='https://api.tinybird.co/v0/pipes/'
    pipe_mv='events_hour_pipe.csv'
    token_mv='p.eyJ1IjogImEyNGY5NWFhLTM3MzMtNGIyNy05NzVkLWRkYmY4OWExZjMyOSIsICJpZCI6ICJmNWM1NThiMS0zZjA3LTRhYzgtYjQ1Mi04OTgzZTU2ZTk1MDcifQ.Y0D-gimVEfcY1hLpEa66uS0ssSX9JKw2NZW-Nk2cFcg'
    
    url=pipes_api+pipe_mv+"?start_date="+start+"&end_date="+end+"&token="+token_mv
    df=pd.read_csv(url)
    
    # chart
    if add_sidebar == 'All events':                                                                       
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
    

        st.plotly_chart(plot, use_container_width=True)
        
    if add_sidebar == 'Single event type':  
        df_event = df[df.event==event]
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df_event.hour, y=df_event.number,
                        mode='lines', 
                        line=dict(color='green',width=1)))
        fig2.update_layout(title=event,
                   xaxis_title='Hour',
                   yaxis_title='Events')
        st.plotly_chart(fig2)

if __name__ == '__main__':
	main()
