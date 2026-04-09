import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    df = pd.read_csv(r"D:\E-commerce data\ecommerce_customer_data_large.csv")
    return df


def clean_data(df):
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    df = df.drop(columns=['Customer Age'])
    df['Returns'] = df['Returns'].fillna(0)
    return df


def analyze_data(df):
    print("商品类别分布：")
    print(df['Product Category'].value_counts())

    print("\n总销售额：", df['Total Purchase Amount'].sum())
    print("平均订单金额：", df['Total Purchase Amount'].mean())

    user_spending = df.groupby('Customer ID')['Total Purchase Amount'].sum()

    print("\nTop10用户：")
    print(user_spending.sort_values(ascending=False).head(10))

    print("\n用户平均消费：", user_spending.mean())

    print("\n流失情况：")
    print(df['Churn'].value_counts())

    print("\n流失 vs 消费：")
    print(df.groupby('Churn')['Total Purchase Amount'].mean())

    print("\n性别流失率：")
    print(df.groupby('Gender')['Churn'].mean())

    print("\n年龄流失率：")
    print(df.groupby('Age')['Churn'].mean())


def visualize(df):
    user_spending = df.groupby('Customer ID')['Total Purchase Amount'].sum()

    user_spending.hist(bins=50)
    plt.title("User Spending Distribution")
    plt.savefig("user_spending.png")
    plt.close()

    df.groupby('Churn')['Total Purchase Amount'].mean().plot(kind='bar')
    plt.title("Churn vs Spending")
    plt.savefig("churn_vs_spending.png")
    plt.close()


def main():
    df = load_data()
    df = clean_data(df)
    analyze_data(df)
    visualize(df)


if __name__ == "__main__":
    main()

