import streamlit as st
import random
st.title("Rock, Paper and Scissors!")

ele=["Rock","Paper","Scissors"]

if "comp_choice" not in st.session_state:
    st.session_state.comp_choice=random.choice(ele)
if "users_choice" not in st.session_state:
    st.session_state.users_choice=None
if "user_count" not in st.session_state:
    st.session_state.user_count=0
if "sys_count" not in st.session_state:
    st.session_state.sys_count=0
if "gameover" not in st.session_state:
    st.session_state.gameover=False


if st.button("Rock"):
    st.session_state.users_choice="Rock"
    st.write("You chose rock")
elif st.button("Paper"):
    st.session_state.users_choice="Paper"
    st.write("You chose Paper")
elif st.button("Scissors"):
    st.session_state.users_choice="Scissors"
    st.write("You chose Scissors")

if st.button("select"):
    if st.session_state.users_choice==st.session_state.comp_choice:
        st.session_state.user_count+=1
        st.success("You Won!...")
        st.session_state.gameover=True
    else:
        st.session_state.sys_count+=1

st.write("Your Score:",st.session_state.user_count)
st.write("My Score:",st.session_state.sys_count)

if st.button("New Game"):
      st.session_state.comp_choice=random.choice(ele)
      st.session_state.gameover=False


