

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import datetime
from storing.data import create_usertable

# <==== Code starts here ====>
st.balloons()

def main():
    st.title('Log in')
    menu=["Home","Login","SignUp"]
    choice=st.sidebar.selectbox("Menu,",menu)
    if choice=="Home":
        st.subheader("Home")
    elif choice=="Login":
        st.subheader("Login Section")
        username=st.sidebar.text_input("User Name")
        password=st.sidebar.text_input("Password",type='password')
        if st.button("Login"):
            st.success("Logged In as {}".format(username))

            task=st.selectbox("Task",["Add Post","Analytics","Profiles"])
            if task=="Add Post":
                st.subheader("Add your Post")
            elif task== "Analytics":
                st.subheader("Analytics")
            elif task== "Profiles":
                st.subheader('User Profile')
            else:
                st.warning("Incorrect Username/Password")

    elif choice=="SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")


if __name__ == '__main__':
	main()



