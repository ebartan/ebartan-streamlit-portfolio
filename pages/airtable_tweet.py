from pyairtable import Api
import streamlit as st
import os
print(st.secrets['AIRTABLE_API_KEY'])
api = Api(st.secrets['AIRTABLE_API_KEY'])
table = api.table('appvyfSdDhwHiySVb', 'tblgKmjwBBxkRfUcy')
all_data = table.all(sort=["-Created"])
print(all_data[0])

# 3 sütun oluştur
col1, col2, col3 = st.columns(3)# Tweet'leri 3'lü gruplara böl ve sütunlarda göster
for i in range(0, len(all_data), 3):
    # İlk sütun
    with col1:
        if i < len(all_data):
            st.text_area("Tweet", 
                        all_data[i]["fields"].get("Tweet_Text", ""), 
                        height=320,
                        key=f"tweet_{i}")
            
            # Image verilerini kontrol et ve varsa göster
            images = all_data[i]["fields"].get("image", [])
            if images and len(images) > 0:
                image_url = images[0].get("url", "")
                if image_url:
                    st.image(image_url, use_container_width=True)
            st.markdown("---")
    
    # İkinci sütun
    with col2:
        if i + 1 < len(all_data):
            st.text_area("Tweet", 
                        all_data[i + 1]["fields"].get("Tweet_Text", ""), 
                        height=320,
                        key=f"tweet_{i+1}")
            
            # Image verilerini kontrol et ve varsa göster
            images = all_data[i + 1]["fields"].get("image", [])
            if images and len(images) > 0:
                image_url = images[0].get("url", "")
                if image_url:
                    st.image(image_url, use_container_width=True)
            st.markdown("---")
    
    # Üçüncü sütun
    with col3:
        if i + 2 < len(all_data):
            st.text_area("Tweet", 
                        all_data[i + 2]["fields"].get("Tweet_Text", ""), 
                        height=320,
                        key=f"tweet_{i+2}")
            
            # Image verilerini kontrol et ve varsa göster
            images = all_data[i + 2]["fields"].get("image", [])
            if images and len(images) > 0:
                image_url = images[0].get("url", "")
                if image_url:
                    st.image(image_url, use_container_width=True)
            st.markdown("---")