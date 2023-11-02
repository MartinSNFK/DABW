import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('Omega 3 with blueberry oatmeal')
streamlit.text('Kale, spinach and rocket Smoothie')
streamlit.text('Hard boiled free range egg')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocade','Strawberries'])

streamlit.dataframe(my_fruit_list)
