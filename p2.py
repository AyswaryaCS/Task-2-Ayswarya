
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "Dataset for Data Analytics.xlsx"
df = pd.read_excel(file_path)

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:", df.isnull().sum().sum())

print("\nNumerical Statistics:")
print(df.describe())

print("\nMean Values:")
print(df.mean(numeric_only=True))

print("\nMedian Values:")
print(df.median(numeric_only=True))

if 'Product' in df.columns:
    print("\nProduct Counts:")
    print(df['Product'].value_counts())

    plt.figure(figsize=(8,5))
    df['Product'].value_counts().plot(kind='bar')
    plt.title('Product Distribution')
    plt.xlabel('Product')
    plt.ylabel('Count')
    plt.show()

if 'PaymentMethod' in df.columns:
    plt.figure(figsize=(6,4))
    df['PaymentMethod'].value_counts().plot(kind='bar')
    plt.title('Payment Method Distribution')
    plt.xlabel('Payment Method')
    plt.ylabel('Count')
    plt.show()

if 'OrderStatus' in df.columns:
    plt.figure(figsize=(6,4))
    df['OrderStatus'].value_counts().plot(kind='bar')
    plt.title('Order Status Distribution')
    plt.xlabel('Order Status')
    plt.ylabel('Count')
    plt.show()

if 'ReferralSource' in df.columns:
    plt.figure(figsize=(6,4))
    df['ReferralSource'].value_counts().plot(kind='bar')
    plt.title('Referral Source Distribution')
    plt.xlabel('Referral Source')
    plt.ylabel('Count')
    plt.show()

if 'TotalPrice' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['TotalPrice'], bins=20, kde=True)
    plt.title('Total Price Distribution')
    plt.xlabel('Total Price')
    plt.ylabel('Frequency')
    plt.show()

if 'TotalPrice' in df.columns:

    Q1 = df['TotalPrice'].quantile(0.25)
    Q3 = df['TotalPrice'].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df['TotalPrice'] < lower_bound) |
                  (df['TotalPrice'] > upper_bound)]

    print("\nNumber of Outliers:", len(outliers))

    plt.figure(figsize=(8,4))
    sns.boxplot(x=df['TotalPrice'])
    plt.title('Boxplot of Total Price')
    plt.show()

print("\nEDA Completed Successfully!")