####One going Data Project###


# Netflix! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.
# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.
# You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!
# You have been supplied with the dataset netflix_data.csv, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
# 1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# 2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

# import pandas as pd
# import matplotlib.pyplot as plt

# #read the file
# netflix_df = pd.read_csv("netflix_data.csv")

# # ##test print first##
# # print(netflix_df) #print ok

# ### 1. What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# # get 1990s column
# # release_year = netflix_df[(netflix_df["release_year"] > 1990) & (netflix_df["release_year"] < 2000)]


# release_year = netflix_df[(netflix_df["release_year"] > 1990) & (netflix_df["release_year"] < 2000)]
# print(release_year)


# #visualize the distribution, set how wide the bars are
# plt.hist(release_year["duration"], bins=50, edgecolor='black')
# plt.title("Distribution of Movie Durations in the 1990s")
# plt.xlabel("Duration(in minutes)")
# plt.ylabel("Frequency")
# plt.show()

# #=====================================
# # 2. A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.


# short_movie_count = netflix_df[netflix_df["duration"] < 90]
# print(short_movie_count)

# # #get column "genre" with only "action"
# movie_df = netflix_df[(netflix_df["genre"] == "Action")]

# # Filter 1990s movies (inclusive 1990–1999)
# movies_90s = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] <= 1999)]

# # Find the most frequent duration
# duration = int(movies_90s["duration"].mode()[0])
# print("Most frequent duration:", duration)

#=====================================
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter the to keep only movies released in the 1990s
# Start by filtering out movies that were released in or after 1990
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# And then do the same to filter out movies released before 2000
movies_1990s = subset[(subset["release_year"] < 2000)]

# Another way to do this step is to use the & operator which allows you to do this type of filtering in one step
# movies_1990s = netflix_subset[(netflix_subset["release_year"] >= 1990) & (netflix_subset["release_year"] < 2000)]

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!
plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

# Filter the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s

# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)

# A quicker way of counting values in a column is to use .sum() on the desired column
# (action_movies_1990s["duration"] < 90).sum()

#==============================================