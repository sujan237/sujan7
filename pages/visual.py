import streamlit as st
import numpy as np
import pandas as pd

with st.container():
   st.write("Visuaization")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

   chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
   st.line_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.scatter_chart(chart_data)


df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)


st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
