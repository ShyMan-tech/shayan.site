import streamlit as st

# -- PAGE SETUP --
about_page = st.Page(
page="views/about_me.py",
title="About Me",
icon=":material/person:",
default=True
)
project_page = st.Page(
page="views/chatbot.py",
title="Chatbot",
icon=":material/smart_toy:",
)

# -- NAVIGATION SETUP --
pg = st.navigation(

    {
        "Info": [about_page],
        "Projects": [project_page]
    }
)

st.logo("assets/logo.png")
st.sidebar.text("Made with ❤️ by Shayan")

# -- RUN NAVIGATION --
pg.run()