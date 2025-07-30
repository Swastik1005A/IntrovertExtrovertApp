import pandas as pd
import numpy as np

df2 = pd.read_csv("test.csv")


df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Stage_fear'] == 'Yes'), 'Time_spent_Alone'] = \
    np.random.uniform(0.0, 3.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Stage_fear'] == 'Yes')].shape[0])

df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Stage_fear'] == 'No'), 'Time_spent_Alone'] = \
    np.random.uniform(4.0, 11.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Stage_fear'] == 'No')].shape[0])

df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Social_event_attendance'] >= 0.0) & (df2['Social_event_attendance'] <= 4.0), 'Time_spent_Alone'] = \
    np.random.uniform(0.0, 3.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Social_event_attendance'] >= 0.0) & (df2['Social_event_attendance'] <= 4.0)].shape[0])

df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Social_event_attendance'] > 4.0) & (df2['Social_event_attendance'] <= 8.0), 'Time_spent_Alone'] = \
    np.random.uniform(4.0, 11.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Social_event_attendance'] > 4.0) & (df2['Social_event_attendance'] <= 8.0)].shape[0])

df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Going_outside'] >= 0.0) & (df2['Going_outside'] <= 2.0), 'Time_spent_Alone'] = \
    np.random.uniform(0.0, 3.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Going_outside'] >= 0.0) & (df2['Going_outside'] <= 2.0)].shape[0])

df2.loc[(df2['Time_spent_Alone'].isnull()) & (df2['Going_outside'] >= 3.0) & (df2['Going_outside'] <= 7.0), 'Time_spent_Alone'] = \
    np.random.uniform(4.0, 11.0, size=df2[(df2['Time_spent_Alone'].isnull()) & (df2['Going_outside'] >= 3.0) & (df2['Going_outside'] <= 7.0)].shape[0])


df2['Time_spent_Alone'] = df2['Time_spent_Alone'].round(0)


df2.loc[(df2['Drained_after_socializing'].isnull()) & (df2['Time_spent_Alone'] <= 3.0), 'Drained_after_socializing'] = 'No'
df2.loc[(df2['Drained_after_socializing'].isnull()) & (df2['Time_spent_Alone'] >= 4.0), 'Drained_after_socializing'] = 'Yes'


df2.loc[(df2['Stage_fear'].isnull()) & (df2['Drained_after_socializing'] == 'No'), 'Stage_fear'] = 'No'
df2.loc[(df2['Stage_fear'].isnull()) & (df2['Drained_after_socializing'] == 'Yes'), 'Stage_fear'] = 'Yes'

df2.loc[
    (df2['Social_event_attendance'].isnull()) & (df2['Stage_fear'] == 'No'),
    'Social_event_attendance'
] = np.random.randint(4, 11, size=df2[(df2['Social_event_attendance'].isnull()) & (df2['Stage_fear'] == 'No')].shape[0])

df2.loc[
    (df2['Social_event_attendance'].isnull()) & (df2['Stage_fear'] == 'Yes'),
    'Social_event_attendance'
] = np.random.randint(0, 4, size=df2[(df2['Social_event_attendance'].isnull()) & (df2['Stage_fear'] == 'Yes')].shape[0])

df2.loc[
    (df2['Going_outside'].isnull()) & (df2['Stage_fear'] == 'No'),
    'Going_outside'
] = np.random.randint(3, 7, size=df2[(df2['Going_outside'].isnull()) & (df2['Stage_fear'] == 'No')].shape[0])

df2.loc[
    (df2['Going_outside'].isnull()) & (df2['Stage_fear'] == 'Yes'),
    'Going_outside'
] = np.random.randint(0, 2, size=df2[(df2['Going_outside'].isnull()) & (df2['Stage_fear'] == 'Yes')].shape[0])

df2.loc[
    (df2['Friends_circle_size'].isnull()) & (df2['Stage_fear'] == 'No'),
    'Friends_circle_size'
] = np.random.randint(6, 15, size=df2[(df2['Friends_circle_size'].isnull()) & (df2['Stage_fear'] == 'No')].shape[0])

df2.loc[
    (df2['Friends_circle_size'].isnull()) & (df2['Stage_fear'] == 'Yes'),
    'Friends_circle_size'
] = np.random.randint(0, 5, size=df2[(df2['Friends_circle_size'].isnull()) & (df2['Stage_fear'] == 'Yes')].shape[0])

df2.loc[
    (df2['Post_frequency'].isnull()) & (df2['Stage_fear'] == 'No'),
    'Post_frequency'
] = np.random.randint(3, 10, size=df2[(df2['Post_frequency'].isnull()) & (df2['Stage_fear'] == 'No')].shape[0])

df2.loc[
    (df2['Post_frequency'].isnull()) & (df2['Stage_fear'] == 'Yes'),
    'Post_frequency'
] = np.random.randint(0, 3, size=df2[(df2['Post_frequency'].isnull()) & (df2['Stage_fear'] == 'Yes')].shape[0])



# df2['Time_spent_Alone'].fillna(round(df2['Time_spent_Alone'].median(), 0), inplace=True)
# df2['Drained_after_socializing'].fillna(df2['Drained_after_socializing'].mode()[0], inplace=True)
# df2['Stage_fear'].fillna(df2['Stage_fear'].mode()[0], inplace=True)
df2['Drained_after_socializing'] = df2['Drained_after_socializing'].map({'Yes': 1.0, 'No': 0.0})
df2['Stage_fear'] = df2['Stage_fear'].map({'Yes': 1.0, 'No': 0.0})


print(df2.isnull().sum())

df2.to_csv("test_cleaned.csv", index=False)
