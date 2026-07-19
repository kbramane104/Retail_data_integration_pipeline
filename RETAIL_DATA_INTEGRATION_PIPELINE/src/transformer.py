def transform_data(df, dataset):

    if dataset == "users" and "email" in df.columns:

        df["email_domain"] = (
            df["email"]
            .str.split("@")
            .str[-1]
        )

    if dataset == "posts" and "title" in df.columns:

        df["title_length"] = df["title"].str.len()

    return df
