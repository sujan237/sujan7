import streamlit as st

def main():
    st.markdown("<h1 style='text-align: center;'>About Sujan Jung Shahi</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.image("https://images.unsplash.com/photo-1681457502728-444c593bb124?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    col2.image("https://images.unsplash.com/photo-1693473812472-a9f1887a6b2d?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    col3.image("https://images.unsplash.com/photo-1693473866807-1c8a100c8138?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

if __name__ == "__main__":
    main()
