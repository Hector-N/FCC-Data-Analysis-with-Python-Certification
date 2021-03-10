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


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #     df_bar = df.copy()
    df_bar = df.copy()

    # add year
    df_bar['year'] = df_bar.index.year
    df_bar.year.value_counts().sort_index()

    # add month name
    df_bar['month'] = df_bar.index.month_name()
    df_bar.month.value_counts(normalize=True).mul(100).round(1)

    # add month index
    df_bar['month_index'] = df_bar.index.month

    # get sorted months
    month_gr = df_bar.groupby('month')
    months_indexes = month_gr.nth(0)
    months_indexes['combo'] = tuple(zip(months_indexes.index, months_indexes.month_index))
    month_tuples = list(months_indexes.combo)
    months_ordered = sorted(month_tuples, key=lambda x: x[1])
    months_ordered = [month for month, index in months_ordered]
    # months_ordered = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # define month as categorical data; Specify logical ordering of the category ---- ordered categories
    month_type = pd.api.types.CategoricalDtype(categories=months_ordered, ordered=True)
    df_bar['month'] = df_bar.month.astype(month_type)

    # data for bar plot
    # todo: make pivot_table instead of this lines
    df_bar.drop(columns='month_index', inplace=True)
    df_bar_gr = df_bar.groupby(['year', 'month'])
    mean = df_bar_gr.mean().sort_index()
    data_for_plot = mean.unstack()
    data_for_plot.columns = months_ordered

    # Draw bar plot
    ax = data_for_plot.plot(kind='bar', figsize=(8, 6), xlabel='Years', ylabel='Average Page Views', legend=True)
    ax.legend(title='Months')
    fig = ax.get_figure()

    # Save image and return fig (don't change this part)
    # todo: issue with saving figure
    fig.savefig('bar_plot.png', dpi=300, transparent=False)
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename({'month': 'Month',
                   'year': 'Year',
                   'value': 'Page Views',
                   'date': 'Date'}, axis=1, inplace=True)

    data_1 = df_box.loc[:, 'Page Views':'Year']
    data_2 = df_box.loc[:, ['Page Views', 'Month']]

    # Set month as category and give it order
    months_abbr = data_2.Month.unique()
    months_abbr_sorted = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months_abbr_type = pd.api.types.CategoricalDtype(categories=months_abbr_sorted, ordered=True)
    data_2['Month'] = data_2.Month.astype(months_abbr_type)

    # Draw box plots (using Seaborn)

    # Combine box plots on one figure
    fig = plt.figure(figsize=(10.0, 5.0))

    axes_1 = fig.add_axes([0, 0, 0.5, 1])
    axes_1.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(x=data_1.Year, y=data_1['Page Views'], data=data_1, ax=axes_1)

    axes_2 = fig.add_axes([0.6, 0.0, 0.5, 1])
    axes_2.set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(x='Month', y='Page Views', data=data_2, ax=axes_2)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


# TODO: MAKE CONCLUSIONS
