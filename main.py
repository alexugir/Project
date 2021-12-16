import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the csv file
df = pd.read_csv('ListaBauturi.csv')
print(df.head())

# Explore the shape of the dataset
print(df.shape)

# Explore the basic information for each column
df.info()

# Drop the irrelevant columns
drop_columns = ['IdProdus', 'Gramaj']
df.drop(drop_columns, axis=1, inplace=True)
print(df.head())

# Explore the basic information for each column
df.info()

# Show the basic statistics of this data set
print(df.describe())

# Discover the statistics of revenue
print(df.Incasari.describe())

# Draw the histogram of the revenue
print(df.Incasari.hist())

# Draw the line char for the change of the revenue
revenues = df.groupby('AnAparitie')['Incasari'].mean()

plt.plot(revenues)
plt.title('The revenue changes from year to year')
plt.xlabel('Year')
plt.ylabel('Revenue')

plt.show()

# Aggregate years into decades
bin_edges = [1990, 2000, 2010, 2015]
bin_names = ['1990s', '2000s', '2010s']
df['Decade'] = pd.cut(df['AnAparitie'], bin_edges, labels=bin_names)
print(df.head())

# Draw the bar chart to compare the revenue of different categories
rev_dis = df.groupby('Categorie').Incasari.mean()

plt.bar(rev_dis.index, rev_dis.values)
plt.title('The comparison of revenue from different categories')
plt.xlabel('Category')
plt.ylabel('Revenue')

plt.show()

# Extract the high revenue dataframe
high_revenue = df.Incasari.quantile(.75)
high_rev_df = df[df.Incasari > high_revenue]
print(high_rev_df.Incasari.describe())

# Draw the scatterplot of the sold amount and revenue
plt.scatter(x=high_rev_df.CantitateVanduta, y=high_rev_df.Incasari)
plt.title('The correlation between Sold Amount and Revenue')
plt.xlabel('Sold Amount')
plt.ylabel('Revenue')

plt.show()

# Calculate the correlation between 'sold amount' and 'revenue'
print(high_rev_df[['CantitateVanduta', 'Incasari']].corr())

# Draw the scatterplot of the price and revenue
plt.scatter(x=high_rev_df.Pret, y=high_rev_df.Incasari)
plt.title('The correlation between Price and Revenue')
plt.xlabel('Price')
plt.ylabel('Revenue')

plt.show()

# Calculate the correlation between 'price' and 'revenue'
print(high_rev_df[['Pret', 'Incasari']].corr())

#which categories are most sold from year to year?
df_categories = df[['AnAparitie', 'Categorie', 'CantitateVanduta']]
print(df_categories.head())

# A function is defined for the selection
def func(group):
    return group.loc[group['CantitateVanduta'] == group['CantitateVanduta'].max()]

#Calculate the mean sold amount for each category in each year
df_pop = df_categories.groupby(['AnAparitie', 'Categorie'], as_index=False).mean()

# Select the most popular category for each year
df_most_pop = df_pop.groupby('AnAparitie', as_index=False).apply(func).reset_index(drop=True)
print(df_most_pop)

# Draw the scatterplot to show the change of the most popular category
plt.scatter(df_most_pop.AnAparitie, df_most_pop.Categorie)
plt.title('The change of the most popular category over the year')
plt.xlabel('Year')
plt.ylabel('Category')

plt.show()

# Draw the pie chart of categories
sizes = df_most_pop.Categorie.value_counts().values
labels = df_most_pop.Categorie.value_counts().index

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')
plt.title('The percentage of each category')

plt.show()

