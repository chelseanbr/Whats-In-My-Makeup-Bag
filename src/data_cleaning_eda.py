def clean_cat_data(df, cols):
    result_df = df.copy()
    for col in cols:
        col_str = 'Cleaned_' + col
        result_df[col_str] = result_df[col].str.lower().str.strip()
    return result_df