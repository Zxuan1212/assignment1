import pandas as pd


def merge_files(input1, input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    merged_df.drop('id', axis=1, inplace=True)
    return merged_df


def drop_missing_rows(df):
    cleaned_df = df.dropna()
    return cleaned_df


def drop_rows_with_insurance(df):
    cleaned_df2 = df[~df['job'].str.contains('insurance|Insurance')]
    return cleaned_df2


def save_cleaned_data(df, output):
    df.to_csv(output, index=False)

merged_df = merge_files('respondent_contact.csv', 'respondent_other.csv')
cleaned_df = drop_missing_rows(merged_df)
cleaned_df2 = drop_rows_with_insurance(cleaned_df)
print(cleaned_df2)