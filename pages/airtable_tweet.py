from pyairtable import Api
import streamlit as st
import os
print(st.secrets['AIRTABLE_API_KEY'])
api = Api(st.secrets['AIRTABLE_API_KEY'])
table = api.table('appvyfSdDhwHiySVb', 'tblgKmjwBBxkRfUcy')
all_data = table.all()
print(all_data)