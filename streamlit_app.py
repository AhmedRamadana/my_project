import streamlit as st
st.title("🎈 My new app")

input1= st.number_input('input1', min_value= 0, max_value=9, value=1 )
input2= st.number_input('input2', min_value= 0, max_value=9, value=1 )
input3= st.number_input('input3', min_value= 0, max_value=9, value=1 )

output = model.predict([[input1,input2,input3]])

st.write("output",output)
