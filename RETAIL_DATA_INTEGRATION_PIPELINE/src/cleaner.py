def clean_data(df):

    df = df.drop_duplicates()

    df = df.dropna(how="all")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df