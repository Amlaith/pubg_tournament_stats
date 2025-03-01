import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.write("# GAZ CUP")

    # Bottom-aligned columns
    col1, col2 = st.columns(2, gap='large')

    # You can also use "with" notation:
    with col1:
        st.subheader('Главное правило')
        st.markdown("""
                    **Смурфинг или стримснайпинг — дисквалификация и бан на будущих турнирах**  
                    *Решение о дисквалификации выносится по усмотрению организатора*
                    """)
                
        st.subheader('Контакты')
        st.markdown("""
                    [https://t.me/gazcupPUBG](https://t.me/gazcupPUBG)
                    [https://discord.gg/gSUJckTg](https://discord.gg/gSUJckTg)
                    [https://www.twitch.tv/gazbro27](https://www.twitch.tv/gazbro27)
                    """)

    with col2:
        st.subheader('Призовой фонд')
        st.markdown("""
                    - 1 место - 5 000 р.
                    - 2 место - 3 000 р.
                    - 3 место - 2 000 р.
                    """)
        
        st.subheader('Игровой процесс')
        st.markdown("""
                    Лобби создаются на европейском сервере в режиме "киберспорт".

                    Название лобби и пароль присылаются в группу капитанов непосредственно перед началом каждого матча.

                    Время ожидания команд в лобби — 5 минут после оповещения капитанов.
                    """)
        
    st.subheader('Подсчет баллов')
    st.markdown("""
                Итоговые баллы = сумма баллов команды за все матчи турнира  
                Баллы за матч = баллы за место в матче + баллы за киллы в матче  

                Баллы за место в матче:  
                - 1 место = 12 баллов  
                - 2 место = 9 баллов  
                - 3 место = 7 баллов  
                - 4 место = 5 баллов  
                - 5 - 6 места = 4 балла  
                - 7 - 8 места = 3 балла  
                - 9 - 12 места = 2 балла  	
                - 13 - 16 места = 1 балл  
                - 17 - 20 места = 0 баллов  

                Баллы за киллы в матче:  		
                - 1 килл = 1 балл  

                Распределение итоговых мест при равенстве баллов у нескольких команд:  
                - Сначала учитывается сумма баллов за места в матчах 
                - Затем учитывается сумма баллов за последний матч  
                - Затем учитывается место, занятое в последнем матче  
                """)
    
    


homepage = st.Page(main, title="Главная страница", icon=":material/home:")
gazcup_1 = st.Page("tournaments_pages/3_GazCup_1.py", title="GAZ CUP #1", icon=":material/table:")
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