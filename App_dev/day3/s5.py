import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.DataFrame(
    {'keyword':['a','b','c','d','e','f','g','h','i','j'],
     'value':[100,200,300,400,500,600,700,800,900,1000]}
)

time_data = pd.DataFrame(
    {
        'data': pd.date_range(start='2025-01-01', periods=30),
        'sales': np.random.randint(10, 100, 30)
    }
)

location_data = pd.DataFrame(
    {
        'lat': [37.5, 37.6, 37.7, 37.8, 37.9, 38.0, 38.1, 38.2, 38.3, 38.4],
        'lon': [127.0, 127.1, 127.2, 127.3, 127.4, 127.5, 127.6, 127.7, 127.8, 127.9]
    }
)

st.line_chart(time_data.set_index('data'))
st.bar_chart(data.set_index('keyword'))
st.map(location_data)

fig = px.bar(data, x='keyword', y='value')
st.plotly_chart(fig)
st.metric('사용자 수', '1234', '접속한 ip기준')