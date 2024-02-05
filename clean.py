import pandas as pd
import pickle

df1 = pd.read_csv('respondent_contact.csv')
df2 = pd.read_csv('respondent_other.csv')
merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
merged_df.drop('id', axis=1, inplace=True)

cleaned_df = merged_df.dropna()

cleaned_df2 = cleaned_df [~cleaned_df ['job'].str.contains('insurance|Insurance')]

with open('dataclean.pkl', 'wb') as file:
    pickle.dump(cleaned_df2, file)