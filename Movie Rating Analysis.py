import numpy as np
import pandas as pd

# this is how you import the data from the file (add engine=python to avoid error)
movies = pd.read_csv("movies.dat", delimiter='::', engine='python')
# print(movies.head())

#In the above code, I have only imported the movies dataset that does not have any column names,
# so let’s define the column names:
movies.columns = ['ID', 'Title', 'Genre']
# print(movies.head())

ratings = pd.read_csv("ratings.dat", delimiter='::', engine='python')
# print(ratings.head())

# define column names
ratings.columns = ['User', 'ID', 'Ratings', 'Timestamp']
# print(ratings.head())

# these two datasets have a common column as ID, which contains movie ID, so we can use this column as the
# common column to merge the two datasets:

data = pd.merge(movies, ratings, on=['ID', 'ID'])
print(data.head())

# the distribution of the ratings of all the movies given by the viewers as a pie chart:
ratings = data['Ratings'].value_counts()
numbers = ratings.index
quantity = ratings.values
import plotly.express as px
fig = px.pie(data, values=quantity, names=numbers)
fig.show()

# let’s take a look at the top 10 movies that got 10 ratings by viewers:
data2 = data.query("Ratings == 10")
print(data2["Title"].value_counts().head(10))