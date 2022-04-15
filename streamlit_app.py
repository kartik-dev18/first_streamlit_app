import streamlit
import pandas as pd
import requests

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_lst = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_lst = my_fruit_lst.set_index('Fruit')


fruits_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_lst.index),['Banana','Apple'])
fruits_to_show = my_fruit_lst.loc[fruits_selected]

#streamlit.dataframe(my_fruit_lst)
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
streamlit.text(fruityvice_response)




