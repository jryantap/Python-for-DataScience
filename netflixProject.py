# Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.
# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.
# You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!
# You have been supplied with the dataset netflix_data.csv, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
# 1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# 2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

import pandas as pd
import matplotlib.pyplot as plt

#read the file
netflix_df = pd.read_csv("netflix_data.csv")

# ##test print first##
# print(netflix_df) #print ok

### 1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# get 1990s column
# release_year = netflix_df[(netflix_df["release_year"] > 1990) & (netflix_df["release_year"] < 2000)]


release_year = netflix_df[(netflix_df["release_year"] > 1990) & (netflix_df["release_year"] < 2000)]
print(release_year)


#visualize the distribution, set how wide the bars are
plt.hist(release_year["duration"], bins=50, edgecolor='black')
plt.title("Distribution of Movie Durations in the 1990s")
plt.xlabel("Duration(in minutes)")
plt.ylabel("Frequency")
plt.show()

#=====================================
# 2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.


# short_movie_count = netflix_df[netflix_df["duration"] < 90]
# print(short_movie_count)

#get column "genre" with only "action"
# movie_df = netflix_df[(netflix_df["genre"] == "Action")]

