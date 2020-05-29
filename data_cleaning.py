# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:58:11 2020

@author: akinmade
"""


import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
remove_kd = salary.apply(lambda x: x.replace('K','').replace('CA$',''))

df['min_salary'] = remove_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = remove_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary'] + df['max_salary'])/2

#cleaning company name
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#cleaning out headquarters 
df['hq_short'] = df['Headquarters'].apply(lambda x: x.split(',')[0])

df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['hq_short'] else 0, axis=1)

#age of company
df['age'] = df['Founded'].apply(lambda x: x if x < 0 else 2020 - x)
#parsing jd

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df['python_yn'].value_counts())

#r studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
print(df['r_yn'].value_counts())

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print(df['aws_yn'].value_counts())

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
print(df['spark_yn'].value_counts())

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(df['excel_yn'].value_counts())


df.to_csv('salary_data_clean.csv', index=False)









































