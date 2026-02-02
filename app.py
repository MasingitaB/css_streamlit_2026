import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Football Coach Profile Page with Match Data for Tournament")

# Collect basic information
name = "Masingita Baloyi"
role = "Head Football Coach"
club = "CHPC FC"

# Display basic profile information
st.header("Coach Overview")
st.write(f"**Name:** {name}")
st.write(f"**Role:** {role}")
st.write(f"**Club:** {club}")

st.image(
    "https://churchsupporthub.org/wp-content/uploads/2024/01/Young-people-playing-football.jpg",
    caption="Football Training Session"
)

# Add a section for achievements
st.header("Team Achievements")
uploaded_file = st.file_uploader("Upload a CSV of Team Achievements", type="csv")

if uploaded_file:
    achievements = pd.read_csv(uploaded_file)
    st.dataframe(achievements)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = achievements[
            achievements.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all achievements")

# Add a section for visualizing achievement trends
st.header("Achievement Trends")
if uploaded_file:
    if "Year" in achievements.columns:
        year_counts = achievements["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add Football Data Section
st.header("Explore Football Data")

# Generate dummy data
match_data = pd.DataFrame({
    "Match": ["Team A vs Team B", "Team C vs Team D", "Team E vs Team F", "Team G vs Team H", "Team I vs Team J"],
    "Goals Scored": [2, 1, 3, 0, 4],
    "Match Date": pd.date_range(start="2024-01-01", periods=5),
})

player_data = pd.DataFrame({
    "Player": ["Messi", "Ronaldo", "Mbappé", "Haaland", "Neymar"],
    "Goals": [30, 28, 25, 32, 20],
    "Appearances": [35, 34, 30, 33, 29],
})

league_data = pd.DataFrame({
    "Team": ["Arsenal", "Barcelona", "Bayern", "PSG", "Manchester City"],
    "Points": [75, 78, 80, 72, 82],
    "Matches Played": [34, 34, 34, 34, 34],
})

# Tabbed view for football data
st.subheader("Football Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore",
    ["Match Results", "Player Statistics", "League Table"]
)

if data_option == "Match Results":
    st.write("### Match Results")
    st.dataframe(match_data)

    goals_filter = st.slider("Filter by Goals Scored", 0, 10, (0, 10))
    filtered_matches = match_data[
        match_data["Goals Scored"].between(goals_filter[0], goals_filter[1])
    ]
    st.write(f"Filtered Results for Goals Range {goals_filter}:")
    st.dataframe(filtered_matches)

elif data_option == "Player Statistics":
    st.write("### Player Statistics")
    st.dataframe(player_data)

    goals_filter = st.slider("Filter by Goals", 0, 40, (0, 40))
    filtered_players = player_data[
        player_data["Goals"].between(goals_filter[0], goals_filter[1])
    ]
    st.write(f"Filtered Results for Goals Range {goals_filter}:")
    st.dataframe(filtered_players)

elif data_option == "League Table":
    st.write("### League Table")
    st.dataframe(league_data)

    points_filter = st.slider("Filter by Points", 0, 100, (0, 100))
    filtered_league = league_data[
        league_data["Points"].between(points_filter[0], points_filter[1])
    ]
    st.write(f"Filtered Results for Points Range {points_filter}:")
    st.dataframe(filtered_league)

# Add a contact section
st.header("Contact Information")
email = "baloyimasingita10@gmail.com"
st.write(f"You can reach {name} at {email}.")
