import pandas as pd
import matplotlib.pyplot as plt

def main():
    moto = pd.read_csv('all_bikez_curated.csv', low_memory=False)

    df = pd.DataFrame(moto, columns=['Engine cylinder', 'Rating']).dropna(subset=['Engine cylinder']).dropna(subset=['Rating'])
    df = df[df['Engine cylinder'].isin(['Electric', 'In-line four', 'Single cylinder', 'V2'])]


    df = pd.DataFrame(df)

    grouped_data = df.groupby('Engine cylinder')['Rating'].mean()
    ax = df['Engine cylinder'].unique()
    plt.bar(ax, grouped_data)
    plt.xlabel('Engine cylinder')
    plt.ylabel('Average rating')
    plt.title('Average rating by engine cylinder')
    plt.show()



if __name__ == "__main__":
        main()