import streamlit

streamlit.title('My first streamlit app')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')
streamlit.text('🥑Avacoda Toast')

streamlit.text('🍌🍓Build Your Own Fruit Smoothie 🍉🍊')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick list to choose the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado', 'Strawberries'])

# display the table in the page
streamlit.dataframe(my_fruit_list)
