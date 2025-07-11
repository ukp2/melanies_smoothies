# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(f"Smoothie App :cup_with_straw:")
st.write(
  """lalala instructions .. 
  """
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('Name on smoothie will be:',name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)




ingredients_list = st.multiselect(
    "Select up to 5:",
    my_dataframe, 
    max_selections=5
)


 # fruit_chosen = counter , loop for

if ingredients_list:

    ingredients_string =''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
        
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
    
    # st.write(my_insert_stmt)
    # st.stop
    
    time_to_insert = st.button('Submit')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        
        st.success('Your Smoothie is ordered!', icon="✅")
