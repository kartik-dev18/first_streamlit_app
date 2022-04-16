import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

streamlit.header('FruityVice Advice For Fruits!!')

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + this_fruit_choice)
  fruity_normalize = pd.json_normalize(fruityvice_response.json())
  return fruity_normalize
  

try :
  fruit_choice = streamlit.text_input('For which fruit you would like to display the info?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get info')
  else :
    bck_frm_fun = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(bck_frm_fun)



except URLError as e:
  streamlit.error()
  
streamlit.write('The User Entered',fruit_choice)

#streamlit.text(fruityvice_response.json())


def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Select * from fruit_load_list")
    return my_cur.fetchall()
  
#Add a button to load fruit
if streamlit.button('Get Fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


streamlit.stop()


    

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# #my_cur.execute("Select CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute("Select * from fruit_load_list")

# #my_data_row = my_cur.fetchone()
# my_data_row = my_cur.fetchall()

# #streamlit.text(my_data_row)
# streamlit.dataframe(my_data_row)






