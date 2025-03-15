import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Untitled design (1).png", width=230)
with col2:
    st.title("Shayan Mallikarjuna", anchor=False)
    st.write(
        " 8th grader | Coder | Python Developer"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

st.write("\n")
st.subheader("Achivements", anchor=False)
st.write(
    """
    - 1st Place for Middle School in CincyHacks 2025
    - 1st Place in the Black History Bowl in Mason Intermediate School
    """
)

st.write("\n")
st.subheader("Hoobies and Interests", anchor=False)
st.write(
    """
    - Coding
    - Gaming
    - Playing Ultimate Frisbee
    - Watching Anime
    """
)