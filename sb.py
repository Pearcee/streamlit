# streamlit_app.py

import streamlit as st
from supabase import create_client, Client

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()

@st.experimental_memo(ttl=600)
def insert_query(name, pet):
    return supabase.table("mytable").insert({"name":name, "pet":pet}).execute()   

name = st.text_input('Name', '')
pet = st.text_input('pet', '')

rows = run_query()

if st.button('Enter '+ name + '  ' + pet):
    insert_query(name, pet)

else:
    st.write('Enter Name & pet')

rows = run_query()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")