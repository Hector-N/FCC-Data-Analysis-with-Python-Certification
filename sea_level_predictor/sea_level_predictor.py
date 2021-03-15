import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from file
    sea = pd.read_csv('epa-sea-level.csv', float_precision='legacy')

    sea.rename({'Year': 'year',
                'CSIRO Adjusted Sea Level': 'CSIRO',
                'Lower Error Bound': 'lower',
                'Upper Error Bound': 'upper',
                'NOAA Adjusted Sea Level': 'NOAA'},
               axis='columns',
               inplace=True)

    # PLOT
    fig = plt.figure(figsize=(16, 8))
    axes = fig.add_axes([0, 0, 1, 1])

    # plot CSIRO data points
    plt.scatter('year', 'CSIRO', data=sea)


    # main line
    # Linear Regression - finds the line of best fit line through your data
    # by searching for the regression coefficient (B1) that minimizes the total error (e) of the model.
    lin = linregress(sea.year, sea.CSIRO)
    x = sea.year
    z = pd.Series(range(2014, 2050, 1), dtype='float')
    x = pd.concat((x, z), axis=0)
    x.sort_values(inplace=True)
    y = (lin.intercept + (lin.slope * x))
    axes.plot(x, y, 'c', lw=4, label='CSIRO best fit line')

    # 2000 line
    data_x_since_2000 = sea.loc[sea.year >= 2000, 'year']
    data_y_since_2000 = sea.loc[sea.year >= 2000, 'CSIRO']
    lin_2000 = linregress(data_x_since_2000, data_y_since_2000)
    x_2000 = pd.Series(range(2000, 2050, 1), dtype='float')
    y_2000 = (lin_2000.intercept + (lin_2000.slope * x_2000))
    axes.plot(x_2000, y_2000, 'g', label='since 2000', lw=4)

    # Add axes attributes
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    axes.set_yticks(list(range(0, 20)))
    axes.set_xlim((1870.0, 2060.0))
    axes.set_ylim((-1.0355688083726844, 16.0))
    axes.legend()

    # axes tuning
    plt.grid()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
