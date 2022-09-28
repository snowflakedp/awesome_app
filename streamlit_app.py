import streamlit
import pandas

streamlit.set_page_config(page_title="HealthyDiner", page_icon=":tada:", layout="wide")
streamlit.title('Welcome to Our the New Healthy Diner :wave:')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# reads in csv and puts into variable my_fruit_list
my_fruit_set = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# create list from fruit column
# my_fruit_list = my_fruit_set.Fruit
my_fruit_set = my_fruit_set.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list))

# displays dataframe
streamlit.dataframe(my_fruit_set)
