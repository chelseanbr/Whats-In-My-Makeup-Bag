def clean_cat_data(df, cols):
    result_df = df.copy()
    for col in cols:
        col_str = 'Cleaned_' + col
        result_df[col_str] = result_df[col].str.lower()
        result_df[col_str] = result_df[col_str].str.strip()
        result_df[col_str] = result_df[col_str].str.replace(',', '')
        result_df[col_str] = result_df[col_str].str.replace('.', '')
    result_df = result_df.drop(cols, axis=1)
    return result_df

def get_count_by_df(df, count_col, groupby_col):
    result_df = df.copy()
    result_df = result_df[[count_col, groupby_col]].drop_duplicates()
    result_df = result_df.groupby(groupby_col).count()
    return result_df