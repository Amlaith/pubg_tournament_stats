import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.subheader("15 февраля 2025")

matches = pd.read_csv('data/matches.csv')
teams = pd.read_csv('data/teams.csv')
players_results = pd.read_csv('data/playersResults.csv')
teams_results = pd.read_csv('data/teamsResults.csv')

matches = matches[matches['tournamentId'] == 1].drop('tournamentId', axis=1)
teams = teams[teams['tournamentId'] == 1].drop('tournamentId', axis=1)
players_results = players_results[players_results['tournamentId'] == 1].drop('tournamentId', axis=1)
teams_results = teams_results[teams_results['tournamentId'] == 1].drop('tournamentId', axis=1)

rank_to_points = [0, 12, 9, 7, 5, 4, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

# Insert containers separated into tabs:
results_tab, matches_tab, players_tab = st.tabs(["Турнирная таблица", "Результаты матчей", "Статистика игроков"])

# You can also use "with" notation:
with results_tab:
    # Место / Команда / Очки за места / Очки за килы / Сумма очков

    teams_results['points'] = teams_results['rank'].apply(lambda rank: rank_to_points[rank])
    rank_points = teams_results.groupby('teamId')['points'].sum()

    kill_points = players_results.groupby('teamId')['kills'].sum()

    res = pd.concat([rank_points, kill_points], axis=1)
    res['total'] = res['points'] + res['kills']
    res = teams.join(res, on='teamId').drop('teamId', axis=1)
    res = res.sort_values('total', ascending=False)
    res = res.set_index(np.arange(1, res.shape[0] + 1))
    res = res.rename(columns={
            'teamName': 'Команда',
            'points': 'Баллы за места',
            'kills': 'Баллы за киллы',
            'total': 'Всего баллов',
        })

    st.table(res)