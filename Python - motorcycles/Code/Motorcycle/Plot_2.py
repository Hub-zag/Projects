import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # read our data frame
    moto = pd.read_csv('all_bikez_curated.csv', low_memory=False)
    data = pd.DataFrame(moto, columns=['Year', 'Category']).dropna(subset=['Category'])
    # one more time we will take only most important categories
    data = data[data['Category'].isin(['Sport', 'Naked', 'Scooter', 'Sport touring', 'Custom / cruiser'])]

    df = pd.DataFrame(data)

    # group by engine cylinder and year, and count the number
    counts = df.groupby(['Category', 'Year']).size().reset_index(name='count')

    # create a separate line chart for each engine cylinder
    for kat in counts['Category'].unique():
        data = counts[counts['Category'] == kat]
        plt.plot(data['Year'], data['count'], label=f'{kat}')

    # make plot more readable
    plt.xlabel('Year')
    plt.ylabel('Number of motorcycles')
    plt.title('Number of motorcycles by category and year')
    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()