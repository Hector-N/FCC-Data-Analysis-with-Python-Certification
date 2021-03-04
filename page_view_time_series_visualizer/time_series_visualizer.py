import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True, index_col='date')

# Clean data
q_975 = df.value.quantile(0.975)
q_025 = df.value.quantile(0.025)
filt_outstanding = (df.value <= q_975) & (df.value >= q_025)
df = df.loc[filt_outstanding, :].copy()


def draw_line_plot():
    # Draw line plot

    fig = plt.figure()

    # plot title
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # axis labels
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # data
    x = df.index
    y = df.value

    plt.plot(x, y)
    # plt.show()
    # plt.savefig('line_plot.png')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df_bar = None
#
#     # Draw bar plot
#
#
#
#
#
#     # Save image and return fig (don't change this part)
#     fig.savefig('bar_plot.png')
#     return fig
#
# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]
#
#     # Draw box plots (using Seaborn)
#
#
#
#
#
#     # Save image and return fig (don't change this part)
#     fig.savefig('box_plot.png')
#     return fig
