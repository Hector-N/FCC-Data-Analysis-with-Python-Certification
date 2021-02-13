import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv', sep=',', index_col=None, )


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()


    # What is the average age of men?
    # average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)


    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df['education'].value_counts(normalize=True).mul(100).round(1).loc['Bachelors']


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu_sal = df[['education', 'salary']]
    higher_education = edu_sal[(edu_sal['education'] == 'Bachelors') |
                               (edu_sal['education'] == 'Masters') |
                               (edu_sal['education'] == 'Doctorate')]
    lower_education = edu_sal[(edu_sal['education'] != 'Bachelors') &
                              (edu_sal['education'] != 'Masters') &
                              (edu_sal['education'] != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = higher_education['salary'].value_counts(normalize=True).mul(100).round(1).loc['>50K']
    lower_education_rich = lower_education['salary'].value_counts(normalize=True).mul(100).round(1).loc['>50K']


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[['salary', 'hours-per-week']][df['hours-per-week'] == min_work_hours]
    rich_percentage = num_min_workers['salary'].value_counts(normalize=True).mul(100).round(1).loc['>50K']


    # todo: review this
    # What country has the highest percentage of people that earn >50K?
    rich_ratio = df.groupby('native-country')['salary'].apply(
        lambda x: x.str.contains('>').sum() / x.str.contains('50').sum() * 100)
    rich_country = rich_ratio[rich_ratio == rich_ratio.max()]
    highest_earning_country = rich_country.index[0]
    highest_earning_country_percentage = round(rich_country[0], 1)


    # todo: review this
    # Identify the most popular occupation for those who earn >50K in India.
    ind = df[(df['native-country'] == 'India')]
    rich_ind = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = rich_ind['occupation'].value_counts().index[0]

    # alt sol
    # go = df.groupby('native-country')['occupation'].value_counts()['India']
    # top_IN_occupation = go.index[0]


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
