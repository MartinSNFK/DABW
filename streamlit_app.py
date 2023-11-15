import streamlit
import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#my_cur.execute("insert into fruit_load_list values (from streamlit')")

#my_cur.execute("SELECT * from fruit_load_list")
streamlit.header('The fruit load list contains:')
#my_data_rows = my_cur.fetchall()
streamlit.dataframe(my_data_rows)

# streamlit.text("The fruit load list contains:")

streamlit.title('My Parents New Healthy Diner')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('Omega 3 with blueberry oatmeal')
streamlit.text('Kale, spinach and rocket Smoothie')
streamlit.text('Hard boiled free range egg')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice")
#comment1 
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#comment2
streamlit.dataframe(fruityvice_normalized)

#streamlit.text(fruityvice_response.json())
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

