import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("⚽ Premier League Dashboard - 2010/11 - 2019/20")
DATA_URL = 'https://raw.githubusercontent.com/tketse/premier-league-datasets/refs/heads/main/epldat10seasons/epl-allseasons-matchstats.csv'


@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)


df = load_data()

st.write("Quick look at the data:")
st.dataframe(df.head())

seasons = df['Season'].unique()
selected_season = st.selectbox("Select a Season", seasons)
filtered_df = df[df['Season'] == selected_season]

filtered_df['TotalGoals'] = filtered_df['HomeGoals'] + filtered_df['AwayGoals']

# Visualization 1: Distribution of total goals per match
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_df['TotalGoals'], bins=range(0, 11), color="orange", edgecolor="black")
ax.set_title("Distribution of Total Goals per Match", fontsize=16)
ax.set_xlabel("Total Goals per Match")
ax.set_ylabel("Number of Matches")
ax.set_xticks(range(0, 11))
st.pyplot(fig)

# Visualization 2: Match results breakdown
results_count = filtered_df['FullTime'].value_counts()

st.subheader("Match Results Breakdown")

fig2, ax2 = plt.subplots()
ax2.pie(results_count, labels=results_count.index, autopct='%1.1f%%')
ax2.set_title("win/Draw Percentages")
st.pyplot(fig2)

# Visualization 3: Teams with most home goals
home_goals = filtered_df.groupby('HomeTeam')['HomeGoals'].sum().sort_values(ascending=False).head(10)

st.subheader("Top 10 Teams with Most Home Goals")

fig3, ax3 = plt.subplots()
ax3.barh(home_goals.index, home_goals.values, color="blue")
ax3.set_xlabel("Total Home Goals")
ax3.invert_yaxis()
st.pyplot(fig3)


