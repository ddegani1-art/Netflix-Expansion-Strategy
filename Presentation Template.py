#!/usr/bin/env python
# coding: utf-8

# <center><h1 style="color:red;">Netflix Expansion Strategy</h1></center>
# 
# ### Claire Owens, Danielle Degani, Jessica Alvino
# #### Group #32
# <center><h4 style="color:green;"> Programming for Business Analytics Presentation</h4></center>
# 
# 
# **Date:** 11/25/25
# 
# **Affiliation:** Binghamton University, School of Management, NY, USA
# 

# ## Agenda
# 
# 1. Introduction
#   
# 2. Problem Statement
# 
#    
# 3. Project Objectives
# 
#    
# 4. Results & Discussions
# 
#    
# 5. Conclusions
# 
# 
# ## Let's Get Started!
# 

# 1. Introduction
#    - Streaming platforms like Netflix rely heavily on data to understand audience preferences and guide decisions about content acquisition and creation. As Netflix expanded globally, its library had to evolve to meet the tastes of a diverse and international subcriber base. This project analyzes how Netflix's content library has changed over time, focusing on genre diversity, the balance between movies and TV shows, and the growing presence of international titles.

# 2. Problem Statement
#    - This project analyzes how Netflix's content library has evolved over time in terms of genre diversity, content type (movies vs. TV), and country of origin, and what these patterns reveal about Netflix's global content expansion strategy.

# 3. Project Objectives
#    - The objective of this project is to analyze Netflix's catalog to identify meaningful trends. Specifically, the project seeks to compare the growth of movies and TV shows over time, examine shifts in genre diversity, and analyze how the platform's country representation has expanded. The goal is to use these findings to interpret Netflix's strategic direction and its response to evolving global audiences.

# In[9]:


import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df.head(50)


# In[14]:


# Check the shape of the dataset (rows, columns)
print(df.shape)

# Check column names and types
print(df.info())

# Quick stats for numeric columns
print(df.describe())

# Count missing values per column
print(df.isnull().sum())


# In[15]:


# -----------------------------
# Step 2: Clean the Netflix Data
# -----------------------------

import pandas as pd

# Convert 'date_added' to datetime (bad values become NaT)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Fill missing 'country' values with "Unknown"
df['country'] = df['country'].fillna("Unknown")

# Fill missing 'director' and 'cast' with "Unknown" (optional)
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")

# Split 'listed_in' column into a list of genres
df['genres'] = df['listed_in'].str.split(', ')

# Split 'country' into a list of countries
df['country_list'] = df['country'].str.split(', ')

# Check the first 10 rows of the cleaned columns
df[['title','type','genres','country_list','date_added']].head(10)


# In[19]:


# Step 3A: Movies vs TV Shows Over Time
# -------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Group data by release year and type
type_trend = df.groupby(['release_year', 'type']).size().reset_index(name='count')

# Plot
plt.figure(figsize=(12,6))
sns.lineplot(data=type_trend, x='release_year', y='count', hue='type', marker="o")

plt.title("Netflix: Movies vs TV Shows Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Content Type")

plt.show()


# In[20]:


# Step 3B: Genre Diversity Over Time
# ----------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Explode genres so each genre is in a separate row
genre_exploded = df.explode('genres')

# Remove empty genres (if any)
genre_exploded = genre_exploded[genre_exploded['genres'].notna()]

# Count titles per genre per year
genre_trend = genre_exploded.groupby(['release_year', 'genres']).size().reset_index(name='count')

# Top 10 genres overall
top_genres = genre_exploded['genres'].value_counts().head(10)
print("Top 10 genres overall:\n", top_genres)

# Filter for top genres for plotting
top_genres_list = top_genres.index.tolist()
genre_trend_top = genre_trend[genre_trend['genres'].isin(top_genres_list)]

# Plot
plt.figure(figsize=(14,7))
sns.lineplot(data=genre_trend_top, x='release_year', y='count', hue='genres')

plt.title("Top Genres Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Genre")

plt.show()


# In[21]:


# Step 3C: Country of Origin Expansion
# ------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Explode countries so each country is in a separate row
country_exploded = df.explode('country_list')

# Remove empty or missing values
country_exploded = country_exploded[country_exploded['country_list'].notna()]
country_exploded = country_exploded[country_exploded['country_list'] != ""]

# Count titles per country per year
country_trend = country_exploded.groupby(['release_year', 'country_list']).size().reset_index(name='count')

# Top 10 countries overall
top_countries = country_exploded['country_list'].value_counts().head(10)
print("Top 10 countries overall:\n", top_countries)

# Filter for only top countries
top_countries_list = top_countries.index.tolist()
country_trend_top = country_trend[country_trend['country_list'].isin(top_countries_list)]

# Plot
plt.figure(figsize=(14,7))
sns.lineplot(data=country_trend_top, x='release_year', y='count', hue='country_list')

plt.title("Netflix Titles from Top Countries Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Country")

plt.show()


# 4. Results & Discussions
#    - The results show a clear shift in Netlflix's content strategy. First, TV shows increased significantly over time, especially after 2015, while movies grew at a slower and more steady pace. This indicates a strategic preference for serialized content that keeps viewers engaged. Genre analysis shows that although Drama and Comedy remain dominant, Netflix has diversified its offerings by adding more International and other genres such as Korean Dramas, Anime, and Reality TV. Additionally, the platform's international content expanded noticeably, with countries like India, South Korea, and the U.K. contributing increasing numbers of titles. These patterns show Netflix's intent to appeal to a global audience and support localized production.

# 5. Conclusions
#    - The findings shoow that Netlflix has transformed from a movie-centered, U.S.-dominated platform into a diverse and global streaming service. The shift toward TV shows, the increase in genre variety, and the rise of international content all highlight Netflix's strategy to capture and retain a worldwide audience. These changes reflect Netflix's broader move toward global expansion, original content production, and diversification of its entertainment library.

# 6. Q&A

# In[ ]:




