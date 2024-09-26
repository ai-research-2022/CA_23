import streamlit as st

# Main title
st.title('Streamlit Layouts Demo')

# Using Columns for layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Hello")

with col2:
    st.header("Column 2")
    st.write("World")

# Using an Expander
with st.expander("See explanation"):
    st.write("Here you could put in some really, really explanatory stuff.")
