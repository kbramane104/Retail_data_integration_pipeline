def validate_data(df):

    return {
        "records": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicates": int(df.astype(str).duplicated().sum()),
    }