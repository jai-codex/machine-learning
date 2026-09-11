import seaborn as sns

# Load dataset
df = sns.load_dataset("titanic")

# See first 5 rows
print(df.head())

# Number of rows and columns
print("Shape:", df.shape)

# Information about columns
print(df.info())

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# Basic statistics
print(df.describe())

# Check target column
print("Survived:")
print(df["survived"].value_counts())