import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Cars93_missing.csv")

print(df.head())

df_indexed = df.set_index("Make")
print(df_indexed.head())

df_condition = df.copy()
df_condition.loc[df_condition["Price"] > 30, "Price"] *= 1.10
print(df_condition[["Price"]].head())

print(df.columns)
print(df.isna().sum())
print(df.isna().sum().sum())


def exchange_columns(dataframe, col1, col2):
    columns = dataframe.columns.tolist()
    i = columns.index(col1)
    j = columns.index(col2)
    columns[i], columns[j] = columns[j], columns[i]
    return dataframe[columns]


df_exchanged = df.copy()
df_exchanged = exchange_columns(df_exchanged, "Price", "Horsepower")
print(df_exchanged.columns.tolist())

df_sorted = df.sort_index(axis=1)
print(df_sorted.columns.tolist())

lower = df["Price"].quantile(0.05)
upper = df["Price"].quantile(0.95)

df_trimmed = df[
    (df["Price"] >= lower) &
    (df["Price"] <= upper)
]

print(df_trimmed.head())

df_filled = df.copy()
df_filled["Horsepower"] = df_filled["Horsepower"].fillna(
    df_filled["Horsepower"].mean()
)

print(df_filled["Horsepower"].head())

dict1 = {
    "Name": ["John", "Peter", "Anna"],
    "Age": [25, 30, 28]
}

dict2 = {
    "City": ["Berlin", "Dortmund", "Hamburg"],
    "Salary": [3000, 3500, 3200]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

df_merged = pd.concat([df1, df2], axis=1)

print(df1)
print(df2)
print(df_merged)

df["Horsepower"].hist(bins=10)
plt.xlabel("Horsepower")
plt.ylabel("Frequency")
plt.title("Horsepower Distribution")
plt.show()

correlation_matrix = df.corr(numeric_only=True)

print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Matrix")
plt.show()
