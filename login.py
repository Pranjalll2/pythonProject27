import streamlit as st


users = {'purvamore@gmail.com': 'FS23AI012', 'pranjalsutar@gmail.com': 'FS23AI021', 'rutuja@gmail.com': 'FS23AI015'}


email = st.text_input('Enter email:')
password = st.text_input('Enter password:', type='password')

# Login button
btn = st.button('Login')

if btn:
    if email in users and password == users[email]:
        st.success('Login Successful!')
        st.balloons()
    else:
        st.error('Login Error: Invalid email or password')