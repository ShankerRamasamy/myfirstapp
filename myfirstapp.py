import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
    

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')





food = st.radio(
     "What's your favorite food",
     ('Pasta', 'Noodles', 'Nasi Lemak'))

if food == 'Pasta':
     st.write('You selected Pasta.')
elif food == 'Noodles':
     st.write('You selected Noodles.')
    
else:
     st.write("You didn't select Pasta or Noodle")
     

st.multiselect('Multiselect', [1,2,3])

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

import datetime

d = st.date_input(
      "When's your birthday",
      datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
