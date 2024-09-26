import pandas as pd
import plotly.express as px
import streamlit as st

# -- Import and clean data (importing csv into pandas)
df = pd.read_csv("https://raw.githubusercontent.com/venomxe/Interactive-Dashboard-of-Bee-Colonies/main/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)

# Streamlit App
st.title("Interactive Dashboard of Bee Colony Health Impacted by Varroa Mites")

# Dropdown for selecting the year
year = st.selectbox(
    "Select Year",
    options=[2015, 2016, 2017, 2018],
    index=0  # Default value is 2015
)

# Filter data based on the selected year and Varroa mites
dff = df[(df["Year"] == year) & (df["Affected by"] == "Varroa_mites")]

# Display the selected year
st.write(f"The year chosen by the user was: {year}")

# Create the choropleth map
fig = px.choropleth(
    data_frame=dff,
    locationmode='USA-states',
    locations='state_code',
    scope="usa",
    color='Pct of Colonies Impacted',
    hover_data=['State', 'Pct of Colonies Impacted'],
    color_continuous_scale=px.colors.sequential.YlOrRd,
    labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
    template='plotly_dark'
)

# Display the plotly map
st.plotly_chart(fig)
