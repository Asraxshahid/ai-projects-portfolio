import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titles.csv")

print(df.head())
print(df.columns)

print(df['type'].value_counts())

genres = df['genres'].value_counts().head(10)
print(genres)

print("\nInsight: Dataset contains both movies and shows with varying genres and release trends.")

type_counts = df['type'].value_counts()

plt.figure()
type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

genres = df['genres'].value_counts().head(10)

plt.figure()
genres.plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

years = df['release_year'].value_counts().head(10)

plt.figure()
years.plot(kind='bar')
plt.title("Top Release Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

