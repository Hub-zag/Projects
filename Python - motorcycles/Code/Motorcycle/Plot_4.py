import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    moto = pd.read_csv("all_bikez_curated.csv", low_memory= False)
    df = pd.DataFrame(moto, columns=['Year', 'Engine cylinder', 'Rating']).dropna(subset=["Engine cylinder"]).dropna(subset=["Rating"])
    df = df[df['Engine cylinder'].isin(['Electric'])]
    df = df.sort_values(by= 'Year')

    counts = df.groupby(['Year'])['Rating'].mean()
    ax = df['Year'].unique()

    plt.plot(ax, counts, marker = 'o')
    plt.xlabel('Year')
    plt.ylabel('Average rating')
    plt.title('Average rating of electric motorcycles')

    plt.show()



if __name__ == "__main__":
    main()