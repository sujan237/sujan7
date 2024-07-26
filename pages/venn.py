import streamlit as st
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3
from io import BytesIO

def plot_venn2(set1, set2, set1_and_2):
    # Create a Venn diagram with 2 sets
    plt.figure(figsize=(8, 6))
    venn2(subsets=(set1, set2, set1_and_2), set_labels=('Set 1', 'Set 2'))
    plt.title('Venn Diagram of 2 Sets')
    return plt

def plot_venn3(set1, set2, set3, set1_and_2, set1_and_3, set2_and_3, set1_and_2_and_3):
    # Create a Venn diagram with 3 sets
    plt.figure(figsize=(10, 8))
    venn3(subsets=(set1, set2, set1_and_2, set3, set1_and_3, set2_and_3, set1_and_2_and_3), 
          set_labels=('Set 1', 'Set 2', 'Set 3'))
    plt.title('Venn Diagram of 3 Sets')
    return plt

st.title('Venn Diagram Generator')

# Select number of sets
num_sets = st.selectbox("Select the number of sets", [2, 3])

if num_sets == 2:
    st.subheader('Enter the elements for the 2 sets Venn Diagram')

    set1 = st.text_input("Elements of Set 1 (comma-separated)")
    set2 = st.text_input("Elements of Set 2 (comma-separated)")
    set1_and_2 = st.text_input("Elements common to both Set 1 and Set 2 (comma-separated)")

    if st.button('Generate Venn Diagram'):
        set1 = set(set1.split(','))
        set2 = set(set2.split(','))
        set1_and_2 = set(set1_and_2.split(','))
        
        venn_plot = plot_venn2(set1, set2, set1_and_2)
        
        buffer = BytesIO()
        venn_plot.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_column_width=True)
        
elif num_sets == 3:
    st.subheader('Enter the elements for the 3 sets Venn Diagram')

    set1 = st.text_input("Elements of Set 1 (comma-separated)")
    set2 = st.text_input("Elements of Set 2 (comma-separated)")
    set3 = st.text_input("Elements of Set 3 (comma-separated)")
    set1_and_2 = st.text_input("Elements common to Set 1 and Set 2 (comma-separated)")
    set1_and_3 = st.text_input("Elements common to Set 1 and Set 3 (comma-separated)")
    set2_and_3 = st.text_input("Elements common to Set 2 and Set 3 (comma-separated)")
    set1_and_2_and_3 = st.text_input("Elements common to Set 1, Set 2, and Set 3 (comma-separated)")

    if st.button('Generate Venn Diagram'):
        set1 = set(set1.split(','))
        set2 = set(set2.split(','))
        set3 = set(set3.split(','))
        set1_and_2 = set(set1_and_2.split(','))
        set1_and_3 = set(set1_and_3.split(','))
        set2_and_3 = set(set2_and_3.split(','))
        set1_and_2_and_3 = set(set1_and_2_and_3.split(','))
        
        venn_plot = plot_venn3(set1, set2, set3, set1_and_2, set1_and_3, set2_and_3, set1_and_2_and_3)
        
        buffer = BytesIO()
        venn_plot.savefig(buffer, format='png')
        buffer.seek(0)
        st.image(buffer, use_column_width=True)
