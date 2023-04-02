import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    # read our data frame
    moto = pd.read_csv('all_bikez_curated.csv', low_memory=False)
    # we will only need 'Year' and 'Engine cylinder'
    df = pd.DataFrame(moto, columns=['Year', 'Engine cylinder']).dropna(subset=['Engine cylinder'])
    # now we take only the most important types of 'Engine cylinder'
    df = df[df['Engine cylinder'].isin(['Electric', 'In-line four', 'Single cylinder', 'V2'])]

    df = pd.DataFrame(df)

    # group by engine cylinder and year, and count the number
    counts = df.groupby(['Engine cylinder', 'Year']).size().reset_index(name='count')

    # create a separate line chart for each engine cylinder
    for cylinder in counts['Engine cylinder'].unique():
        data = counts[counts['Engine cylinder'] == cylinder]
        plt.plot(data['Year'], data['count'], label=f'{cylinder}')

    # make this plot more readable
    plt.xlabel('Year')
    plt.ylabel('Number of motorcycles')
    plt.title('Number of motorcycles by engine cylinder and year')
    plt.legend()

    # show the plot
    plt.show()
if __name__ == '__main__':
    main()