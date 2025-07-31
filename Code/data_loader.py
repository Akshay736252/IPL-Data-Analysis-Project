import pandas as pd

def load_excel(filepath):
    """
    Loads Excel or CSV file using pandas.
    """
    try:
        if filepath.endswith('.xlsx') or filepath.endswith('.xls'):
            return pd.read_excel(filepath)
        elif filepath.endswith('.csv'):
            return pd.read_csv(filepath)
        else:
            print("Unsupported file format.")
            return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

