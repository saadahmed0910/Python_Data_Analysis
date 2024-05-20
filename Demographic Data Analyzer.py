#!/usr/bin/env python
# coding: utf-8

# In[185]:


import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == "Male", 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    actual = (df['education']).value_counts()
    
    percentage_bachelors = round((actual['Bachelors']/actual.sum())*100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    above_50k = df[df["salary"] == ">50K"]
    all_education = (above_50k['education'].count().sum())
    
    #For higher_education_rich
    degree_no_money = df['education'].value_counts()
    
    low_bachelors = degree_no_money['Bachelors'].sum()
    low_masters = degree_no_money['Masters'].sum()
    low_doctorate = degree_no_money['Doctorate'].sum()
    low_degree_sum = low_bachelors + low_masters + low_doctorate
    
    
    with_degree = (above_50k['education']).value_counts()
    with_bachelors = with_degree['Bachelors'].sum()
    with_masters = with_degree['Masters'].sum()
    with_doctorate = with_degree['Doctorate'].sum()
    #--------------------------------------------------------------------
    
    drop_list = ('Bachelors', 'Masters', 'Doctorate')
    data_frame = df[~(df['education'].isin(drop_list))]
    
    
    without_rich = (data_frame['salary'] == ">50K").value_counts()[1]
    test = data_frame[data_frame['education'] == 'Bachelors'].count().sum()

    without_degree = (data_frame['education']).count().sum()
    
    
    percent_advanced = (with_bachelors + with_masters + with_doctorate / with_degree.sum()) * 100
    percent_without = (without_degree / (without_degree + all_education)) * 100
    
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = actual["Bachelors"].sum() + actual["Masters"].sum() + actual["Doctorate"].sum()
    lower_education = (data_frame['education'].value_counts().sum())

    # percentage with salary >50K
    higher_education_rich = round(((with_bachelors + with_masters + with_doctorate) / low_degree_sum) * 100, 1)
    lower_education_rich = round((without_rich / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = ((num_min_workers[num_min_workers['salary'] == '>50K'].count().sum()) / num_min_workers.count().sum()) * 100

    # What country has the highest percentage of people that earn >50K?
    amount_high_country = above_50k['native-country'].value_counts()
    total_country = df['native-country'].value_counts()

    
    new_df = df[['salary', 'native-country']]
    new_above_50k = new_df[new_df['salary'] == '>50K']

    #print(new_above_50k.value_counts())
    #print(new_df['native-country'].value_counts())

    the_country = (new_above_50k['native-country'].value_counts() / new_df['native-country'].value_counts())
    the_answer = pd.DataFrame({'country':the_country.index, 'percentage':the_country.values})

    name_country = the_answer.loc[the_answer['percentage'] == the_country.max()]
    name_list  = name_country.iloc[0][0]
    
    
    
    highest_earning_country = name_list
    #print(highest_earning_country)
    highest_earning_country_percentage = round(((amount_high_country / total_country).max()) * 100, 1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df['occupation'].mode() [0]

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
calculate_demographic_data(print_data = True)

