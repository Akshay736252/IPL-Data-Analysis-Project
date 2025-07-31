def clean_column_names(df):
    """
    Removes leading/trailing spaces and replaces special characters in column names.
    """
    df.columns = (
        df.columns.str.strip()               # remove spaces
                  .str.replace(" ", "_")     # spaces to underscores
                  .str.replace(r'[^\w\s]', '', regex=True)  # remove special characters
    )
    return df
