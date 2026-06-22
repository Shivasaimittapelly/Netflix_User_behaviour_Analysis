#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')


# In[3]:


# Load Data set 

df = pd.read_csv('netflix_titles.csv')

df.head()


# In[4]:


# Check Data 

df.info()


# In[6]:


#Check data 

df.shape


# In[7]:


# Data cleaning 
## Check Missing values 

df.isnull().sum()


# In[8]:


# Filling null values 

df['director'] = df['director'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')


# In[9]:


# Remove Duplicates 

df.drop_duplicates(inplace=True)


# In[11]:


# EDA 

df['type'].value_counts()


# In[12]:


# Visualization 
sns.countplot(x='type', data=df)
plt.title("Movies vs TV Shows")
plt.show()


# In[13]:


# Content Ratings 

plt.figure(figsize=(10,5))

sns.countplot(
    y=df['rating'],
    order=df['rating'].value_counts().index
)

plt.title("Content Ratings")
plt.show()


# In[16]:


# Release Year trend 


import pandas as pd
import seaborn as sns

print("Pandas:", pd.__version__)
print("Seaborn:", sns.__version__)

plt.figure(figsize=(12,5))

plt.hist(df['release_year'], bins=30)

plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows/Movies")

plt.grid(True)

plt.show()


# In[18]:


# Split Generes 

genres = df['listed_in'].str.split(', ', expand=True)

genres.head()


# In[22]:


# Count Genere
from collections import Counter

genre_count = Counter()

for genre_list in df['listed_in']:
    for genre in genre_list.split(', '):
        genre_count[genre] += 1
        
# Create Data Frame 

genre_df = pd.DataFrame(
    genre_count.items(),
    columns=['Genre','Count']
)

genre_df = genre_df.sort_values(
    by='Count',
    ascending=False
)

genre_df.head()


# In[23]:


# Visualization 


plt.figure(figsize=(12,6))

sns.barplot(
    x='Count',
    y='Genre',
    data=genre_df.head(10)
)

plt.title("Top 10 Genres")
plt.show()


# In[25]:


# Step 8 Top Countries Producing Content 

country_count = df['country'].value_counts().head(10)

country_count.plot(
    kind='bar'
)

plt.title("Top Countries")
plt.show()


# In[30]:


# Step 9: Content Added Over Time

df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='mixed',
    errors='coerce'
)


# In[31]:


df['year_added'] = df['date_added'].dt.year


# In[32]:


df['year_added'].value_counts().sort_index().plot()

plt.title("Content Added Over Time")
plt.show()


# In[33]:


# Step 10: Correlation Analysis

numeric_df = df[['release_year']]


# In[34]:


# Correlation 
corr = numeric_df.corr()

sns.heatmap(
    corr,
    annot=True
)

plt.show()


# In[35]:


# Step 11: Business Insights



# Write observations like:

# Insight 1

# Movies are more common than TV Shows.

# Insight 2

# TV-MA is the most frequent rating.

# Insight 3

# Drama and International Movies are top genres.

# Insight 4

# USA contributes the most content.

# Insight 5

# Netflix rapidly expanded content after 2015.


# In[ ]:





# In[ ]:




