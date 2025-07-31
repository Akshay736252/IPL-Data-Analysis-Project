def get_total_runs(df):
    return df['Runs'].sum()

def get_average_runs(df):
    return df['Runs'].mean()

def get_total_centuries(df):
    return df[df['Runs'] >= 100].shape[0]

