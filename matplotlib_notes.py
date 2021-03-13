from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# # Matplotlib - plotting library for Python
# # Data science + visualize data
#
# # predefined styles
# print(plt.style.available)
# plt.style.use('fivethirtyeight')
#
# # comic style
# # plt.xkcd()
#
# # naming plot, setting axes
# plt.title('median salary (usd) by age')
# plt.xlabel('ages')
# plt.ylabel('median salary')
#
# # show grid
# plt.grid(True)
#
# # adjust padding in case of small screens
# # plt.tight_layout()
#
# # # Median Developer Salaries by Age
# # ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# # dev_y = [38496, 42000, 46752, 49320, 53200,
# #          56000, 62316, 64928, 67317, 68748, 73752]
# # plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', linewidth=3, label='All Devs')
# #
# # # Median Python Developer Salaries by Age
# # py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# # py_dev_y = [45372, 48876, 53850, 57287, 63016,
# #             65998, 70003, 70000, 71496, 75370, 83640]
# # plt.plot(ages_x, py_dev_y, color='b', marker='o', label='Python')
# #
# # # Median JavaScript Developer Salaries by Age
# # js_dev_y = [37810, 43515, 46823, 49293, 53437,
# #             56373, 62375, 66674, 68745, 68746, 74583]
# # plt.plot(ages_x, js_dev_y, color='g', linestyle=':', marker='*', label='JavaScript')
#
#
# # Ages 18 to 55
# ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
# py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
#             84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
# js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
#             78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
# dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
#          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
# plt.plot(ages_x, dev_y, color='k', linestyle='--', marker='.', linewidth=3, label='All Devs')
# plt.plot(ages_x, py_dev_y, color='b', marker='o', label='Python')
# plt.plot(ages_x, js_dev_y, color='g', linestyle=':', marker='*', label='JavaScript')
#
# plt.legend()
#
# # output plot
# plt.show()
#
# # save plot
# # plt.savefig('plot_01.png')
#
# # 2 ways of adding legends
# # 1 - add list of labels in order as they added to the plot
# # plt.legend(['All devs', 'Python devs'])
# # 2 - pass a 'label' arg to a 'plot' method + call `plt.legend()` without args
# # method 2 is less errorprone
#
# # customizing the look
# # 1 - use format string - '[marker][line][color]'
# # 2 - pass as arguments
#
# # types of plots
# # line plot,


# vid 2 - BAR CHARTS
# Median Developer Salaries by Age

# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexes = np.arange(len(ages_x))
# width = 0.25  # define width of the bar
#
# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All dev')
#
# # Median Python Developer Salaries by Age
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width, label='Python')
#
# # Median JavaScript Developer Salaries by Age
# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_indexes + width, js_dev_y, width=width, label='JavaScript')
#
# plt.legend()
# plt.xticks(ticks=x_indexes, labels=ages_x)  # fix x labels
#
#
# plt.title('Median salary by age')
# plt.xlabel('Ages')
# plt.ylabel('Salaries')
# plt.tight_layout()
# plt.show()


# vid 3 - pie charts
# chows a proportion of the category to the whole set
# plt.title('Pie Chart')
# plt.style.use('fivethirtyeight')
# plt.tight_layout()
# plt.show()
#
# slices = [6987358970, 48739578980]
# labels = ['label_x', 'label_z']
# colors = ['red', 'green']
# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

# # real example
# # Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java',]
# explode = [0, 0, 0, 0.1, 0]
# plt.title('Language Popularity (Pie Chart)')
# plt.pie(slices, labels=labels, explode=explode, wedgeprops={'edgecolor': 'white'},
#         shadow=True, startangle=90, autopct='%1.1f%%')
#
# plt.style.use('fivethirtyeight')
# plt.tight_layout()
# plt.show()
#



# vid 4 - STACK PLOT (AREA PLOT)
# similar to the pie-chart
# shows how the proportions of the different value contribute to the whole, but shows it 'over time'
#
# minutes = list(range(1, 10))
# # player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# # player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# # player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
# player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
# player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
# player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
# # plt.pie([1,1,1], labels=[player1, player2, player3])
# plt.title('PieChart Players')
# plt.stackplot(minutes, player1, player2, player3, labels=['1', '2', '3'])
# plt.legend(loc='upper left')
# plt.tight_layout()
# plt.show()


# # vid 5 - add fills to line plots
# data = pd.read_csv('data.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']
#
# plt.plot(ages, dev_salaries, color='#444444',
#          linestyle='--', label='All Devs')
#
# plt.plot(ages, py_salaries, label='Python')
#
# # overall_median = 57287
#
# plt.legend()
#
# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')
#
# plt.tight_layout()
#
# plt.show()
#




# dummy monkey patching
def aa            (a, b):
        return a * b

pd.DataFrame = aa

n = pd.DataFrame(10, 5)
















