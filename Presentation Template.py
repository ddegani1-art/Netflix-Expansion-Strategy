#!/usr/bin/env python
# coding: utf-8

# <center><h1 style="color:red;">Netflix Expansion Strategy</h1></center>
# 
# ### Claire Owens, Danielle Degani, Jessica Alvino
# <center><h4 style="color:green;"> Programming for Business Analytics Presentation</h4></center>
# 
# 
# **Date:** 11/25/25
# 
# **Affiliation:** Binghamton University, School of Management, NY, USA
# 

#!/usr/bin/env python
# coding: utf-8

# --- Netflix Expansion Strategy Dashboard ---
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# Streamlit Page Setup
# --------------------------------------------
st.set_page_config(page_title="Netflix Expansion Strategy", layout="wide")
st.title("Netflix Expansion Strategy Dashboard")
st.write("""
Claire Owens, Danielle Degani, Jessica Alvino  
**Group #32 – Programming for Business Analytics Presentation**  
_Binghamton University, School of Management, NY, USA_
""")

# --------------------------------------------
# Load Data
# --------------------------------------------
df = pd.read_csv("netflix_titles.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

# --------------------------------------------
# Step 2: Clean the Netflix Data
# --------------------------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['country'] = df['country'].fillna("Unknown")
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['genres'] = df['listed_in'].str.split(', ')
df['country_list'] = df['country'].str.split(', ')

st.success("Data cleaned")

# --------------------------------------------
# Step 3A: Movies vs TV Shows Over Time
# --------------------------------------------
st.header("Movies vs TV Shows Over Time")
type_trend = df.groupby(['release_year', 'type']).size().reset_index(name='count')

plt.figure(figsize=(12,6))
sns.lineplot(data=type_trend, x='release_year', y='count', hue='type', marker="o")
plt.title("Netflix: Movies vs TV Shows Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
st.pyplot(plt)

# --------------------------------------------
# Step 3B: Genre Diversity Over Time
# --------------------------------------------
st.header("Genre Diversity Over Time")
genre_exploded = df.explode('genres')
genre_exploded = genre_exploded[genre_exploded['genres'].notna()]
genre_trend = genre_exploded.groupby(['release_year', 'genres']).size().reset_index(name='count')

top_genres = genre_exploded['genres'].value_counts().head(10)
st.subheader("Top 10 Genres Overall")
st.dataframe(top_genres)

top_genres_list = top_genres.index.tolist()
genre_trend_top = genre_trend[genre_trend['genres'].isin(top_genres_list)]

plt.figure(figsize=(14,7))
sns.lineplot(data=genre_trend_top, x='release_year', y='count', hue='genres')
plt.title("Top Genres Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
st.pyplot(plt)

# --------------------------------------------
# Step 3C: Country of Origin Expansion
# --------------------------------------------
st.header("Country of Origin Expansion")
country_exploded = df.explode('country_list')
country_exploded = country_exploded[country_exploded['country_list'].notna()]
country_exploded = country_exploded[country_exploded['country_list'] != ""]

country_trend = country_exploded.groupby(['release_year', 'country_list']).size().reset_index(name='count')
top_countries = country_exploded['country_list'].value_counts().head(10)

st.subheader("Top 10 Countries Overall")
st.dataframe(top_countries)

top_countries_list = top_countries.index.tolist()
country_trend_top = country_trend[country_trend['country_list'].isin(top_countries_list)]

plt.figure(figsize=(14,7))
sns.lineplot(data=country_trend_top, x='release_year', y='count', hue='country_list')
plt.title("Netflix Titles from Top Countries Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
st.pyplot(plt)

# --------------------------------------------
# Conclusion
# --------------------------------------------
st.header("Conclusions")
st.write("""
Netflix’s content library has evolved dramatically over time:
- **TV shows** have grown rapidly, especially post-2015.
- **Genre diversity** has expanded beyond drama and comedy.
- **Global reach** increased, with major contributions from India, the UK, and South Korea.

These findings highlight Netflix’s strategy to appeal to a global audience by diversifying its content offerings.
""")
