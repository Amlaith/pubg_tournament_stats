import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.write("# GAZ CUP")

    # st.sidebar.success("Select a demo above.")


homepage = st.Page(main, title="Главная страница")
gazcup_1 = st.Page("tournaments_pages/3_GazCup_1.py", title="GAZ CUP #1", icon=":material/trophy:")
gazcup_2a = st.Page("tournaments_pages/1_GazCup_2a.py", title="GAZ CUP #2, лобби A", icon=":material/trophy:")
gazcup_2b = st.Page("tournaments_pages/2_GazCup_2b.py", title="GAZ CUP #2, лобби B", icon=":material/trophy:")


pg = st.navigation(
        {
            "GAZ CUP": [homepage],
            "Актуальные турниры": [gazcup_2a, gazcup_2b],
            "Архив": [gazcup_1],
        }
    )

pg.run()