import streamlit as st

st.sidebar.subheader("15 февраля 2025")


# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Турнирная таблица", "Статистика игроков"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
    st.radio("Select one:", [1, 2])