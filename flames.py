import streamlit as st

st.title("🔥 FLAMES")

name1 = st.text_input("Enter the first name")
name2 = st.text_input("Enter the second name")

if st.button("Get Result"):
    if name1 and name2:

        a = list(name1.lower())
        b = list(name2.lower())

        for i in a.copy():
            if i in b:
                a.remove(i)
                b.remove(i)

        n = len(a + b)

        s = "flames"
        while len(s) != 1:
            i = (n % len(s)) - 1
            if i == -1:
                s = s[:-1]
            else:
                s = s[i+1:] + s[:i]

        d = {
            'f': 'Friends',
            'l': 'Love',
            'a': 'Attraction',
            'm': 'Marriage',
            'e': 'Engaged',
            's': 'Siblings'
        }

        st.success(f"💖 Relationship Result: **{d[s]}**")

    else:
        st.warning("Please enter both names")
