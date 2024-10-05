import streamlit as st


st.markdown("<h1 style='text-align: center;'>About Me 👋</h1>", unsafe_allow_html=True)


col1,col2 = st.columns(2)

with col1:
    st.image(image="pages/images/developer-dribbble.gif")

with col2:
    st.markdown("""
    ### Name: Lalit Mahale 
    (ML Engineer)

    ##### Follow me  👇: 
                
    Linkedin : https://www.linkedin.com/in/lalitmahale1997/
                
    Github : https://github.com/LalitMahale
                
    Portfolio : https://lalitmahale.github.io/
    """)