import datetime
from datetime import date
import streamlit as st
from pandas_datareader import data
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

cos = ["AAPL","MSFT","TSLA", "IUKD.L", "BABA", "VWRL.L"]
end   = date.today()
start = end.replace(year=end.year-3)


st.set_page_config(
   page_title="Money",
   page_icon="💲",
   layout= "wide", #"centered",
   initial_sidebar_state = "auto",
   menu_items={
      'Get Help': 'https://www.extremelycoolapp.com/help',
      'Report a bug': "https://www.extremelycoolapp.com/bug",
      'About': "# This is a header. This is an *extremely* cool app!"
   },
)

col1, col2, col3 = st.columns(3)

with col1:
    start = st.date_input(
        "Start Date",
        start )

with col2:
    end = st.date_input(
        "End Date",
        end )

with col3:
    options = st.multiselect(
     'Shares',
     cos,
     "AAPL")

st.header("Stocks from %s %s for %s" %  (start, end, options))

for co in options:
    st.write(co)
    trend = data.DataReader(co, 
        start= start, 
        end=end, 
        data_source='yahoo')['Adj Close']

    st.line_chart(trend)

print(trend)
chart = pd.DataFrame(trend)

st.write(chart)

