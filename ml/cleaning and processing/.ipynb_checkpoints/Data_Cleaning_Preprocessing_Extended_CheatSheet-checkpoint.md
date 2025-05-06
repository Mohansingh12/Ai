
# 🧼 Data Cleaning & Preprocessing Cheat Sheet (Python)

This guide helps you understand **what**, **why**, and **how** of data cleaning and preprocessing using Python libraries like Pandas, NumPy, and Scikit-learn.

---

## 📁 1. Load & Inspect Data

### 🔹 Why?
Before processing, you need to understand the data's structure, data types, and any obvious issues.

```python
import pandas as pd

df = pd.read_csv("data.csv")      # Load CSV file
df.head()                         # See first few rows
df.info()                         # Get data types and non-null counts
df.describe()                     # Basic statistics of numeric columns
df.columns                        # Column names
df.shape                          # (rows, columns)
```

---

## 🔍 2. Handling Missing Data

### 🔹 Why?
Missing values can cause model errors or misleading results. Handle them before model training.

```python
df.isnull().sum()                 # Count missing values per column
df.dropna()                       # Drop rows with missing values
df.fillna(0)                      # Replace missing with 0
df.fillna(method='ffill')        # Forward-fill previous value
df['col'].fillna(df['col'].mean())  # Replace with column mean
```

> ✅ Choose method based on context. Don't blindly drop rows!

---

## 🧹 3. Remove Duplicates & Unwanted Columns

### 🔹 Why?
Duplicates bias model training; irrelevant columns add noise.

```python
df.duplicated().sum()            # Check duplicate rows
df.drop_duplicates(inplace=True) # Remove them
df.drop(['col1', 'col2'], axis=1, inplace=True)  # Drop unnecessary columns
```

---

## 🔁 4. Data Type Conversion

### 🔹 Why?
Models expect consistent data types (e.g., numeric for ML), and operations like date extraction require datetime types.

```python
df['col'] = df['col'].astype('int')
df['date'] = pd.to_datetime(df['date'])
```

---

## 🏷️ 5. Categorical Encoding

### 🔹 Why?
ML models can’t work directly with text labels. Encoding converts them to numeric form.

```python
# Label Encoding (Ordinal relationships)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category'] = le.fit_transform(df['category'])

# One-Hot Encoding (No order)
df = pd.get_dummies(df, columns=['category_col'])
```

> 📌 One-hot is better when no ordinal relationship exists.

---

## 🔢 6. Feature Scaling

### 🔹 Why?
Algorithms like SVM, KNN, and Gradient Descent are sensitive to feature scale.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standardization (mean=0, std=1)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['col1', 'col2']])

# Normalization (0 to 1)
minmax = MinMaxScaler()
df_normalized = minmax.fit_transform(df[['col1', 'col2']])
```

---

## 📏 7. Outlier Detection & Removal

### 🔹 Why?
Outliers can skew the model and reduce accuracy.

```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['col'] >= Q1 - 1.5 * IQR) & (df['col'] <= Q3 + 1.5 * IQR)]
```

> ⚠️ Don't always remove outliers. Understand why they're present.

---

## 🧠 8. Feature Engineering

### 🔹 Why?
Creating new meaningful features helps models find better patterns.

```python
df['new_feature'] = df['col1'] * df['col2']  # Example interaction feature

# Extract parts of date
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.weekday
```

> 🛠️ Feature engineering often has more impact than choosing complex models.

---

## 🔀 9. Train-Test Split

### 🔹 Why?
To test your model's generalization ability on unseen data.

```python
from sklearn.model_selection import train_test_split

X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## 📊 10. Visual Checks

### 🔹 Why?
Visualization helps you detect patterns, missing data, and outliers.

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.isnull(), cbar=False)   # Missing data heatmap
sns.pairplot(df)                       # Relationships between features
df['col'].hist()                       # Histogram
```

---

## ✅ Useful Tips
- Always back up the original data.
- Use `pipeline` or `ColumnTransformer` from `sklearn` for production workflows.
- Use `sklearn.impute.SimpleImputer` for advanced imputation strategies.
- Consider using libraries like `feature-engine`, `missingno`, `sweetviz` for enhanced EDA.

---

## 📦 Libraries Used
- `pandas` – Data manipulation
- `numpy` – Math operations
- `sklearn.preprocessing` – Scaling & encoding
- `matplotlib`/`seaborn` – Data visualization

---

Happy Cleaning! 🚀
