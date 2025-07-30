import pandas as pd

import numpy as np

df1 = pd.read_csv("train.csv")


# Fill missing values in StageFear
df1.loc[(df1['Stage_fear'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Stage_fear'] = 'No'
df1.loc[(df1['Stage_fear'].isnull()) & (df1['Personality'] == 'Introvert'), 'Stage_fear'] = 'Yes'



df1.loc[(df1['Time_spent_Alone'].isnull()) & (df1['Personality'] == 'Introvert'), 'Time_spent_Alone'] = \
    np.random.uniform(4.0, 11.0, size=df1[(df1['Time_spent_Alone'].isnull()) & (df1['Personality'] == 'Introvert')].shape[0])

df1.loc[(df1['Time_spent_Alone'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Time_spent_Alone'] = \
    np.random.uniform(0.0, 3.0, size=df1[(df1['Time_spent_Alone'].isnull()) & (df1['Personality'] == 'Extrovert')].shape[0])

df1.loc[(df1['Social_event_attendance'].isnull()) & (df1['Personality'] == 'Introvert'), 'Social_event_attendance'] = \
    np.random.uniform(0.0, 4.0, size=df1[(df1['Social_event_attendance'].isnull()) & (df1['Personality'] == 'Introvert')].shape[0])

df1.loc[(df1['Social_event_attendance'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Social_event_attendance'] = \
    np.random.uniform(5.0, 10.0, size=df1[(df1['Social_event_attendance'].isnull()) & (df1['Personality'] == 'Extrovert')].shape[0])

df1.loc[(df1['Going_outside'].isnull()) & (df1['Personality'] == 'Introvert'), 'Going_outside'] = \
    np.random.uniform(0.0, 2.0, size=df1[(df1['Going_outside'].isnull()) & (df1['Personality'] == 'Introvert')].shape[0])

df1.loc[(df1['Going_outside'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Going_outside'] = \
    np.random.uniform(3.0, 7.0, size=df1[(df1['Going_outside'].isnull()) & (df1['Personality'] == 'Extrovert')].shape[0])

df1.loc[(df1['Drained_after_socializing'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Drained_after_socializing'] = 'No'
df1.loc[(df1['Drained_after_socializing'].isnull()) & (df1['Personality'] == 'Introvert'), 'Drained_after_socializing'] = 'Yes'

df1.loc[(df1['Friends_circle_size'].isnull()) & (df1['Personality'] == 'Introvert'), 'Friends_circle_size'] = \
    np.random.uniform(0.0, 4.0, size=df1[(df1['Friends_circle_size'].isnull()) & (df1['Personality'] == 'Introvert')].shape[0])

df1.loc[(df1['Friends_circle_size'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Friends_circle_size'] = \
    np.random.uniform(5.0, 15.0, size=df1[(df1['Friends_circle_size'].isnull()) & (df1['Personality'] == 'Extrovert')].shape[0])

df1.loc[(df1['Post_frequency'].isnull()) & (df1['Personality'] == 'Introvert'), 'Post_frequency'] = \
    np.random.uniform(0.0, 5.0, size=df1[(df1['Post_frequency'].isnull()) & (df1['Personality'] == 'Introvert')].shape[0])

df1.loc[(df1['Post_frequency'].isnull()) & (df1['Personality'] == 'Extrovert'), 'Post_frequency'] = \
    np.random.uniform(6.0, 10.0, size=df1[(df1['Post_frequency'].isnull()) & (df1['Personality'] == 'Extrovert')].shape[0])

# df1['Stage_fear'] = df1['Stage_fear'].astype(float64)
# df1['Drained_after_socializing'] = df1['Drained_after_socializing'].astype(float64)

df1['Drained_after_socializing'] = df1['Drained_after_socializing'].map({'Yes': 1.0, 'No': 0.0})
df1['Stage_fear'] = df1['Stage_fear'].map({'Yes': 1.0, 'No': 0.0})
df1['Personality'] = df1['Personality'].map({'Introvert': 1.0, 'Extrovert': 0.0})

df1['Time_spent_Alone'] = df1['Time_spent_Alone'].round(0)
df1['Social_event_attendance'] = df1['Social_event_attendance'].round(0)
df1['Going_outside'] = df1['Going_outside'].round(0)
df1['Drained_after_socializing'] = df1['Drained_after_socializing'].round(0)
df1['Friends_circle_size'] = df1['Friends_circle_size'].round(0)
df1['Post_frequency'] = df1['Post_frequency'].round(0)






print(df1.isnull().sum())
df1.to_csv("train_cleaned.csv", index=False)

