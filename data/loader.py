import pandas as pd

def load_properties(path="data/properties.csv"):
    df = pd.read_csv(path)
    df["content"] = df.apply(
        lambda x: f"{x.title} in {x.location}, Price: {x.price}, {x.bhk} BHK. {x.description}",
        axis=1
    )
    return df