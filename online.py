import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
   page_title="Steve",
   page_icon="😎",
   layout= "wide", #"centered",
   initial_sidebar_state = "auto",
   menu_items={
      'Get Help': 'https://www.extremelycoolapp.com/help',
      'Report a bug': "https://www.extremelycoolapp.com/bug",
      'About': "# This is a header. This is an *extremely* cool app!"
   },
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')

)

x = st.slider('x') +10 # 👈 this is a widget
st.write(x, 'squared is', x * x)

chart_data = pd.DataFrame(
     np.random.randn(x, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



map_data = pd.DataFrame(
    np.random.randn(x * 10, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])


st.map(map_data)

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
if st.checkbox('Show dataframe'):
  map_data

  st.write(pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 20, 30, 40]
  }))