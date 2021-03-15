import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    sea = pd.read_csv('epa-sea-level.csv')

    sea.rename({'Year': 'year',
                'CSIRO Adjusted Sea Level': 'CSIRO',
                'Lower Error Bound': 'lower',
                'Upper Error Bound': 'upper',
                'NOAA Adjusted Sea Level': 'NOAA'},
               axis='columns',
               inplace=True)

    # Create scatter plot

    fig = plt.figure(figsize=(16, 8))
    axes = fig.add_axes([0, 0, 1, 1])

    # Add axes attributes
    axes.set_title('Rise in Sea Level')
    axes.set_xlabel('Year')
    axes.set_ylabel('Sea Level (inches)')
    axes.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    axes.set_yticks(list(range(0, 20)))

    axes.set_xlim((1870.0, 2060.0))
    axes.set_ylim((-1.0355688083726844, 16.0))

    # axes tuning
    plt.grid()

    # plot CSIRO data
    plt.scatter('year', 'CSIRO', data=sea)

    # Linear Regression
    # finds the line of best fit line through your data
    # by searching for the regression coefficient (B1) that minimizes the total error (e) of the model.

    def extended(ax, x, y, **args):
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        x_ext = np.linspace(xlim[0], xlim[1], 100)
        p = np.polyfit(x, y, deg=1)

        y_ext = np.poly1d(p)(x_ext)
        ax.plot(x_ext, y_ext, **args)

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        return ax

    lin = linregress(sea.year, sea.CSIRO)
    # plt.plot(sea.year, (lin.intercept + lin.slope * sea.year), 'c', lw=4)

    x = sea.year
    y = (lin.intercept + lin.slope * sea.year)

    axes.plot(x, y, 'c', lw=4, label='CSIRO best fit line')
    axes = extended(axes, x, y, color="r", lw=1, label="Extended CSIRO best fit line")

    data_x_2000 = sea.loc[sea.year >= 2000, 'year']
    data_y_2000 = sea.loc[sea.year >= 2000, 'CSIRO']
    lin2000 = linregress(data_x_2000, data_y_2000)
    x_2 = data_x_2000.copy()
    y_2 = lin2000.intercept + lin2000.slope * x_2

    axes.plot(x_2, y_2, 'g', label='2000', lw=4)
    axes = extended(axes, x_2, y_2, color="r", lw=1, label="Extended 2000")

    axes.legend()

    # Create second line of best fit

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    # return fig



# def draw_plot():
#
    # # Read data from file
    # sea = pd.read_csv('epa-sea-level.csv')
    #
    # sea.rename({'Year': 'year',
    #             'CSIRO Adjusted Sea Level': 'CSIRO',
    #             'Lower Error Bound': 'lower',
    #             'Upper Error Bound': 'upper',
    #             'NOAA Adjusted Sea Level': 'NOAA'},
    #            axis='columns',
    #            inplace=True)
#
#     # Create scatter plot
#
#     # create figure and axes
#     fig = plt.figure(figsize=(16, 8))
#     axes = fig.add_axes([0, 0, 1, 1])
#
#     # Add axes attributes
#     axes.set_title('Rise in Sea Level')
#     axes.set_xlabel('Year')
#     axes.set_ylabel('Sea Level (inches)')
#     axes.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
#     axes.set_yticks(list(range(0, 12)))
#
#     axes.set_xlim((1870.0, 2060.0))
#     axes.set_ylim((-1.0355688083726844, 11.0))
#
#     # axes tuning
#     plt.grid()
#
#     # plot CSIRO data
#     plt.scatter('year', 'CSIRO', data=sea)
#
#     # Linear Regression
#     # finds the line of best fit line through your data
#     # by searching for the regression coefficient (B1) that minimizes the total error (e) of the model.
#
#     def extended(ax, x, y, **args):
#         xlim = ax.get_xlim()
#         ylim = ax.get_ylim()
#
#         x_ext = np.linspace(xlim[0], xlim[1], 100)
#         p = np.polyfit(x, y, deg=1)
#
#         y_ext = np.poly1d(p)(x_ext)
#         ax.plot(x_ext, y_ext, **args)
#
#         ax.set_xlim(xlim)
#         ax.set_ylim(ylim)
#
#         return ax
#
#     lin = linregress(sea.year, sea.CSIRO)
#     # plt.plot(sea.year, (lin.intercept + lin.slope * sea.year), 'c', lw=4)
#
#     x = sea.year
#     y = (lin.intercept + lin.slope * sea.year)
#
#     axes = extended(axes, x, y, color="r", lw=1, label="Extendes CSIRO best fit line")
#
#     axes.plot(x, y, 'c', lw=4, label='CSIRO best fit line')
#
#     axes.legend()
#
#     # Create first line of best fit
#
#     #     axes = extended(axes, [1925, 1950, 1975], [1, 5, 8],  color="r", lw=1, label="extended")
#     #     axes.plot([1925, 1950, 1975], [1, 5, 8], color="g", lw=4, label="short")
#
#     #     axes = extended(axes, [1925, 1950, 1975], [1, 5, 8],  color="r", lw=1, label="extended")
#     #     axes.plot([1925, 1950, 1975], [1, 5, 8], color="g", lw=4, label="short")
#
#     # Create second line of best fit
#
#     # Save plot and return data for testing
#     plt.savefig('sea_level_plot.png')
#     return plt.gca()
#     # return fig


# def draw_plot():
#     # Read data from file
# 
# 
#     # Create scatter plot
# 
# 
#     # Create first line of best fit
# 
# 
#     # Create second line of best fit
# 
# 
#     # Add labels and title
# 
#     
#     # Save plot and return data for testing (DO NOT MODIFY)
#     plt.savefig('sea_level_plot.png')
#     return plt.gca()