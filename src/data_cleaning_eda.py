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