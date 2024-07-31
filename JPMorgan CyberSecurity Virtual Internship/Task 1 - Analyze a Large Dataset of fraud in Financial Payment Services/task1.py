import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return list(df)

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(n=k)

def exercise_4(df):
    return df['type'].unique()

def exercise_5(df):
    return df['nameDest'].value_counts().head(10)

def exercise_6(df):
    return df[df['isFraud'] == 1]

def exercise_7(df):
    pass

def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()
    def transaction_counts_split_by_fraud(df):
        return df.groupby(by=['type', 'isFraud']).size()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Frequency of Transaction Types')
    axs[0].set_xlabel('Transaction Types')
    axs[0].set_ylabel('Number of Occurrence')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Frequency of Transaction Types, Split by Fraud')
    axs[1].set_xlabel('Transaction Types, Fraud')
    axs[1].set_ylabel('Number of Occurrence')
    fig.suptitle('Transaction Types')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return "The number of transactions varies based on the data, but what's important is that fraud only happens in CASH_OUT and TRANSFER transactions. This helps management know where to focus their manual reviews, which can reduce missed fraud"


def visual_2(df):
    def query(df):
        df['Beginning Delta'] = df['oldbalanceOrg'] -	df['newbalanceOrig']
        df['Destination Delta'] = df['oldbalanceDest'] -	df['newbalanceDest']
        return df[df['type']=='CASH_OUT']
    plot = query(df).plot.scatter(x='Beginning Delta',y='Destination Delta')
    plot.set_title('Begnning v. Destination Balance Delta for Cash Out Transactions')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return "A cash out happens when someone takes out money. It's good to see activity in only two of the four sections because if all four had activity, it would mean there's a problem with the data. The y=-x line is especially important because it shows instant settlement"

def exercise_custom(df):
    return df[['isFlaggedFraud', 'isFraud']].value_counts()
    
def visual_custom(df):
    fig, ax = plt.subplots(1, figsize=(4,6))
    exercise_custom(df).plot(ax=ax, kind='bar')
    ax.set_title('Detected Fraud graph')
    ax.set_xlabel('Is-FlaggedFraud, Is-Fraud')
    ax.set_ylabel('Number of Occurrence')
    for i in ax.patches:
        ax.annotate(i.get_height(), (i.get_x(), i.get_height()))
    return "Here, we see that the fraud detection system misses almost all the fraud. However, it doesn't give any false alarms. This might mean that the system only reports fraud when it's very sure about it"
    


df = exercise_0('transactions.csv')
# Test exercises here
exercise_1(df)
exercise_2(df, 8)
exercise_3(df, 6)
exercise_4(df)
exercise_5(df)
exercise_6(df)

visual_1(df)
visual_2(df)
visual_custom(df)