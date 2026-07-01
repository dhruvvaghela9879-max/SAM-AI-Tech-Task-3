import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("E:\Python\project\Zomatodata.csv")

# Create dashboard
plt.figure(figsize=(18,12))

# 1. Top 10 Restaurants by Votes
top_votes = df.sort_values("Votes", ascending=False).head(10)

plt.subplot(2,3,2)
plt.bar(top_votes["Restaurant_Name"], top_votes["Votes"])
plt.title("Top 10 Restaurants by Votes")
plt.xticks(rotation=70)

# 2. Pie Chart – Cuisine Distribution
cuisine = df["Cuisine"].value_counts().head(5)

plt.subplot(2,3,3)
plt.pie(cuisine.values,
        labels=cuisine.index,
        autopct='%1.1f%%',
        startangle=90)
plt.title("Top 5 Cuisine Distribution")

# 3. Horizontal Bar Chart – Top Rated Restaurants
top_rating = (
    df.groupby("Restaurant_Name")["Avg_Rating_Restaurant"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.subplot(2,3,6)
plt.barh(top_rating.index, top_rating.values)
plt.title("Top 10 Rated Restaurants")
plt.xlabel("Average Rating")

# 4. Histogram – Restaurant Ratings
plt.subplot(2,3,4)
plt.hist(df["Avg_Rating_Restaurant"], bins=10)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")

# 5. Scatter Plot – Votes vs Rating
plt.subplot(2,3,1)
plt.scatter(df["Votes"], df["Avg_Rating_Restaurant"])
plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")

plt.tight_layout()
plt.show()