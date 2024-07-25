import streamlit as st

def main():
    st.title('CV Builder')

    # Input fields
    st.header('Personal Information')
    first_name = st.text_input('First Name')
    last_name = st.text_input('Last Name')
    email = st.text_input('Email')
    phone = st.text_input('Phone')

    st.header('Education')
    education = st.text_area('Education')

    st.header('Experience')
    experience = st.text_area('Experience')

    st.header('Skills')
    skills = st.text_area('Skills')

    st.header('Projects')
    projects = st.text_area('Projects')

    if st.button('Generate CV'):
        # Display the CV
        st.subheader('Curriculum Vitae')
        st.write(f"Name: {first_name} {last_name}")
        st.write(f"Email: {email}")
        st.write(f"Phone: {phone}")

        st.subheader('Education')
        st.write(education)

        st.subheader('Experience')
        st.write(experience)

        st.subheader('Skills')
        st.write(skills)

        st.subheader('Projects')
        st.write(projects)

if __name__ == '__main__':
    main()
