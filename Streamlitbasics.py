import streamlit as st
st.title("BASIC TITLE")
st.header("header part")
st.text("this part contains basic text ")
st.markdown("***bold text** and *Italic text* ")

option=st.radio('select a option:',['M','E','N'])
st.write("you selected",option)

# dropdown box
city=st.selectbox("select city",['Delhi','mumbai','bangalore'])
st.write(f"you chose {city}")

name=st.text_input("enter you name:")
st.write("hello ",name)

#dateinput
#timeinput
#dataframe
#table
#metric
#barchart
#sidebar
