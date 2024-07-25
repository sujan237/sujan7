import streamlit as st
import numpy as np

with st.container():
   st.write("Visuaization")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))
